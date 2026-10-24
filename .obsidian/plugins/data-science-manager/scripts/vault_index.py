"""数据科学知识库的本地 LanceDB 索引。协议输出只写 stdout，诊断只写 stderr。"""

from __future__ import annotations

import argparse
from collections import Counter
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
from typing import Any


SCHEMA_VERSION = 1
TABLE_NAME = "notes"
DIMENSIONS = 1024
KINDS = ("experiment", "project", "exercise", "concept", "source")
TOPIC_DIRS = {
    "01 - 概率论": ("probability-theory", "概率论"),
    "02 - 数理统计": ("mathematical-statistics", "数理统计"),
    "03 - 线性代数与优化": ("linear-algebra-optimization", "线性代数与优化"),
    "04 - 统计学习": ("statistical-learning", "统计学习"),
    "05 - 概率模型与推断": ("probabilistic-models", "概率模型与推断"),
    "06 - 深度学习": ("deep-learning", "深度学习"),
    "07 - 因果推断与实验": ("causal-inference", "因果推断与实验"),
    "08 - 随机过程与时间序列": ("stochastic-processes", "随机过程与时间序列"),
    "09 - 数据计算与可复现性": ("data-computing", "数据计算与可复现性"),
}
NOTE_ROOTS = (*TOPIC_DIRS, "00 - 首页/教材归档", "10 - 项目与案例")
PUBLIC_FIELDS = ("path", "title", "kind", "topic", "topic_label", "status",
                 "difficulty", "source_id", "source_exercise", "excerpt")
FILTER_FIELDS = ("kind", "topic", "status", "source_id")


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return ""


def normalized_list(value: Any) -> list[str]:
    values = value if isinstance(value, list) else ([value] if value else [])
    return [v.strip().lstrip("#") for v in values if isinstance(v, str) and v.strip()]


def excerpt(body: str) -> str:
    text = re.sub(r"```.*?```", " ", body, flags=re.S)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"(?m)^\s*>?\s*(?:#{1,6}\s*|\[![^\]]+\][-+]?\s*)", "", text)
    return re.sub(r"\s+", " ", text).strip()[:260]


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


class VaultIndex:
    def __init__(self, vault: str | Path, db_dir: str | Path,
                 model: str | Path | None = None, device: str = "auto"):
        self.vault = Path(vault).resolve()
        self.db_dir = Path(db_dir).resolve()
        if not self.vault.is_dir():
            raise ValueError("知识库目录不存在")
        if self.db_dir == self.vault or not self.db_dir.is_relative_to(self.vault):
            raise ValueError("索引目录必须是当前知识库内部的独立子目录")
        self.model_dir = Path(model).resolve() if model else None
        self.device = device
        self.owner_file = self.db_dir / ".data-science-index.json"
        self._db = None
        self._model = None
        self._loaded_model_signature = ""

    def checked_note_path(self, path: str | Path) -> Path:
        candidate = Path(path)
        if not candidate.is_absolute():
            candidate = self.vault / candidate
        resolved = candidate.resolve()
        if not resolved.is_relative_to(self.vault) or resolved.suffix.lower() != ".md":
            raise ValueError("笔记路径必须指向当前知识库内的 Markdown 文件")
        return resolved

    def parse_note(self, path: Path) -> dict | None:
        path = self.checked_note_path(path)
        relative = path.relative_to(self.vault)
        if any(part.startswith(".") for part in relative.parts):
            return None
        raw = path.read_bytes()
        text = raw.decode("utf-8-sig")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            return None
        with redirect_stdout(sys.stderr):
            import yaml
            try:
                meta = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError as exc:
                raise ValueError(f"笔记元数据无法安全解析：{relative.as_posix()}") from exc
        if not isinstance(meta, dict):
            raise ValueError(f"笔记元数据必须是字段映射：{relative.as_posix()}")
        tags = normalized_list(meta.get("tags"))
        kind = next((kind for kind in KINDS if kind in tags), "")
        if not kind:
            return None
        body = text[match.end():].strip()
        title = scalar(meta.get("title")) or path.stem
        fallback_topic, fallback_label = TOPIC_DIRS.get(relative.parts[0], ("", ""))
        links = [m.group(1).replace(r"\|", "|").split("|", 1)[0].split("#", 1)[0].strip()
                 for m in re.finditer(r"\[\[([^\]]+)\]\]", body)]
        links = list(dict.fromkeys(link for link in links if link))
        aliases = normalized_list(meta.get("aliases"))
        record = {
            "path": relative.as_posix(), "title": title, "kind": kind,
            "topic": scalar(meta.get("topic")) or fallback_topic,
            "topic_label": scalar(meta.get("topic_label")) or fallback_label,
            "status": scalar(meta.get("status")), "difficulty": scalar(meta.get("difficulty")),
            "source_id": scalar(meta.get("source_id")),
            "source_exercise": scalar(meta.get("source_exercise")),
            "source_kind": scalar(meta.get("source_kind")),
            "archive_status": scalar(meta.get("archive_status")),
            "tags": tags, "links": links, "body": body, "excerpt": excerpt(body),
            "file_hash": hashlib.sha256(raw).hexdigest(), "mtime": path.stat().st_mtime,
            "search_text": "\n".join([title, " ".join(aliases), " ".join(tags),
                                        scalar(meta.get("source_id")), body]),
            "vector": None, "vector_model": "",
        }
        return record

    def scan(self) -> dict[str, dict]:
        records = {}
        for relative in NOTE_ROOTS:
            scope = self.vault / relative
            if not scope.is_dir():
                continue
            resolved_scope = scope.resolve()
            if not resolved_scope.is_relative_to(self.vault):
                raise ValueError(f"索引范围不能链接到知识库外：{relative}")
            for path in sorted(scope.rglob("*.md")):
                if any(part.startswith(".") for part in path.relative_to(scope).parts):
                    continue
                resolved = path.resolve()
                if not resolved.is_relative_to(resolved_scope):
                    raise ValueError(f"笔记链接超出所属索引范围：{path.name}")
                record = self.parse_note(path)
                if record:
                    records[record["path"]] = record
        return records

    def _metadata(self) -> dict:
        if not self.owner_file.exists():
            return {}
        data = json.loads(self.owner_file.read_text(encoding="utf-8"))
        if data.get("vault") != str(self.vault) or data.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("索引归属或版本不匹配；不会覆盖其他知识库的索引")
        return data

    def _write_metadata(self, data: dict):
        data.update(vault=str(self.vault), schema_version=SCHEMA_VERSION)
        self.owner_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def _connect(self, create: bool = False):
        self._metadata()
        if not self.owner_file.exists():
            if not create:
                raise ValueError("尚未建立本库索引，请先点击同步索引")
            if self.db_dir.exists() and any(self.db_dir.iterdir()):
                raise ValueError("目标目录已有未归属本插件的数据，已停止写入")
            self.db_dir.mkdir(parents=True, exist_ok=True)
            self._write_metadata({})
        if self._db is None:
            with redirect_stdout(sys.stderr):
                import lancedb
                self._db = lancedb.connect(str(self.db_dir))
        return self._db

    @staticmethod
    def schema():
        with redirect_stdout(sys.stderr):
            import pyarrow as pa
        fields = [pa.field(name, pa.string()) for name in (
            "path", "title", "kind", "topic", "topic_label", "status", "difficulty",
            "source_id", "source_exercise", "source_kind", "archive_status", "body",
            "excerpt", "file_hash", "search_text", "vector_model")]
        fields.extend([pa.field("tags", pa.list_(pa.string())),
                       pa.field("links", pa.list_(pa.string())),
                       pa.field("mtime", pa.float64()),
                       pa.field("vector", pa.list_(pa.float32(), DIMENSIONS), nullable=True)])
        return pa.schema(fields)

    def _table(self, create=False):
        db = self._connect(create=create)
        if TABLE_NAME not in db.list_tables().tables:
            if not create:
                raise ValueError("尚未建立笔记表，请先同步索引")
            return db.create_table(TABLE_NAME, schema=self.schema())
        table = db.open_table(TABLE_NAME)
        if not table.schema.equals(self.schema(), check_metadata=False):
            raise ValueError("已有笔记表结构与本插件不一致，已停止写入")
        return table

    def model_signature(self) -> str:
        if self.model_dir is None:
            return ""
        weights = self.model_dir / "model.safetensors"
        if not weights.is_file():
            return ""
        info = weights.stat()
        return f"{self.model_dir}|{info.st_size}|{info.st_mtime_ns}|bge-m3:1024:max2048"

    def _load_model(self):
        signature = self.model_signature()
        if not signature:
            raise ValueError("找不到完整的本地 bge-m3 模型；可先使用关键词索引，本插件不会下载模型")
        if self._model is not None and self._loaded_model_signature != signature:
            raise ValueError("模型文件在运行中发生变化，请重启插件后重新同步语义索引")
        if self._model is None:
            print("正在加载本地 bge-m3 嵌入模型……", file=sys.stderr, flush=True)
            os.environ["HF_HUB_OFFLINE"] = "1"
            os.environ["TRANSFORMERS_OFFLINE"] = "1"
            os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
            with redirect_stdout(sys.stderr):
                import torch
                from sentence_transformers import SentenceTransformer
                device = ("cuda:0" if torch.cuda.is_available() else "cpu") if self.device == "auto" else self.device
                self._model = SentenceTransformer(
                    str(self.model_dir), device=device, local_files_only=True,
                    model_kwargs={"use_safetensors": True})
                self._model.max_seq_length = 2048
                self._loaded_model_signature = signature
        return self._model

    def _embed(self, texts: list[str]) -> list[list[float]]:
        model = self._load_model()
        with redirect_stdout(sys.stderr):
            vectors = model.encode(texts, batch_size=4, normalize_embeddings=True,
                                   show_progress_bar=False, convert_to_numpy=True)
        result = vectors.tolist()
        if any(len(vector) != DIMENSIONS for vector in result):
            raise ValueError("本插件需要 1024 维 bge-m3 嵌入；模型输出维数不一致")
        if any(not math.isfinite(value) for vector in result for value in vector):
            raise ValueError("嵌入模型返回非有限数值，已停止写入语义索引")
        return result

    @staticmethod
    def _counts(rows: list[dict]) -> dict:
        return dict(Counter(row["kind"] for row in rows))

    def status(self) -> dict:
        meta = self._metadata()
        exists = bool(meta and (self.db_dir / f"{TABLE_NAME}.lance").is_dir())
        total = int(meta.get("total", 0)) if exists else 0
        return {"exists": exists, "total": total,
                "counts": meta.get("counts", {}) if exists else {},
                "last_sync": meta.get("last_sync", ""),
                "semantic_ready": bool(exists and total and meta.get("semantic_count") == total
                                       and meta.get("model_signature") == self.model_signature()),
                "model_available": bool(self.model_signature()), "schema_version": SCHEMA_VERSION}

    def sync(self, semantic: bool = True) -> dict:
        current = self.scan()  # 原文或 YAML 有问题时先停止，不误删已有索引。
        table = self._table(create=True)
        old = {row["path"]: row for row in table.to_arrow().to_pylist()}
        added = [path for path in current if path not in old]
        updated = [path for path in current if path in old and current[path]["file_hash"] != old[path]["file_hash"]]
        deleted = [path for path in old if path not in current]
        changed = set(added + updated)
        signature = self.model_signature()
        to_write = []
        for path, row in current.items():
            if path not in changed:
                row["vector"], row["vector_model"] = old[path]["vector"], old[path]["vector_model"]
            if path in changed:
                to_write.append(row)
        to_embed = []
        if semantic:
            if current and not signature:
                raise ValueError("本地 bge-m3 模型不可用；可取消语义索引后先同步关键词索引")
            to_embed = [row for row in current.values() if row["vector"] is None or row["vector_model"] != signature]
            if to_embed:
                print(f"正在为 {len(to_embed)} 篇笔记生成真实嵌入……", file=sys.stderr, flush=True)
                vectors = self._embed([("\n".join([row["title"]] * 3) + "\n" + row["body"]) for row in to_embed])
                for row, vector in zip(to_embed, vectors):
                    row["vector"], row["vector_model"] = vector, signature
                    if row["path"] not in changed:
                        to_write.append(row)
        if to_write:
            with redirect_stdout(sys.stderr):
                import pyarrow as pa
                payload = pa.Table.from_pylist(to_write, schema=self.schema())
                # LanceDB 0.37 把 null 也视为待处理的向量；显式保留 null，
                # 表示“尚未生成真实嵌入”，不可用填零冒充语义向量。
                table.merge_insert("path").when_matched_update_all().when_not_matched_insert_all().execute(
                    payload, on_bad_vectors="null")
        for path in deleted:
            table.delete("path = " + sql_literal(path))
        rows = list(current.values())
        semantic_count = sum(row["vector"] is not None and row["vector_model"] == signature for row in rows)
        meta = {"total": len(rows), "counts": self._counts(rows),
                "last_sync": datetime.now(timezone.utc).isoformat(),
                "model_signature": signature, "semantic_count": semantic_count}
        self._write_metadata(meta)
        return {**meta, "added": len(added), "updated": len(updated), "deleted": len(deleted),
                "unchanged": len(current) - len(added) - len(updated),
                "embedded": len(to_embed), "semantic_ready": bool(rows and semantic_count == len(rows))}

    @staticmethod
    def _filtered(rows: list[dict], request: dict) -> list[dict]:
        for field in FILTER_FIELDS:
            value = request.get(field)
            if value:
                rows = [row for row in rows if row.get(field) == str(value)]
        return rows

    @staticmethod
    def _public(row: dict, score: float = 0, query: str = "") -> dict:
        item = {field: row.get(field, "") for field in PUBLIC_FIELDS}
        if query:
            low = row.get("body", "").casefold()
            token = next((token for token in query.casefold().split() if token in low), "")
            if token:
                start = max(0, low.index(token) - 55)
                item["excerpt"] = excerpt(row["body"][start:start + 360])
        item["score"] = round(float(score), 6)
        return item

    def search(self, request: dict) -> dict:
        query = str(request.get("query", "")).strip()
        mode = str(request.get("mode", "keyword"))
        if mode not in {"keyword", "semantic"}:
            raise ValueError("检索模式仅支持 keyword 或 semantic")
        limit = max(1, min(100, int(request.get("limit", 30))))
        table = self._table()
        rows = self._filtered(table.to_arrow().to_pylist(), request)
        if not query or mode == "keyword":
            tokens = query.casefold().split()
            matches = []
            for row in rows:
                text, title = row["search_text"].casefold(), row["title"].casefold()
                if all(token in text for token in tokens):
                    score = sum(6 * int(token in title) + min(text.count(token), 5) for token in tokens)
                    matches.append((score, row))
            matches.sort(key=lambda item: (-item[0], item[1]["title"].casefold(), item[1]["path"]))
            return {"items": [self._public(row, score, query) for score, row in matches[:limit]],
                    "total": len(matches), "mode": "keyword"}
        signature = self.model_signature()
        eligible = [row for row in rows if row["vector"] is not None and row["vector_model"] == signature]
        if not eligible:
            raise ValueError("当前筛选范围没有可用的语义向量，请先同步语义索引")
        vector = self._embed([query])[0]
        conditions = ["vector IS NOT NULL", "vector_model = " + sql_literal(signature)]
        conditions.extend(field + " = " + sql_literal(str(request[field])) for field in FILTER_FIELDS if request.get(field))
        hits = table.search(vector).metric("cosine").where(" AND ".join(conditions), prefilter=True).limit(limit).to_list()
        return {"items": [self._public(row, 1 - float(row.get("_distance", 0)), query) for row in hits],
                "total": len(eligible), "mode": "semantic"}

    def related(self, request: dict) -> dict:
        target = self.checked_note_path(str(request.get("path", ""))).relative_to(self.vault).as_posix()
        rows = self._table().to_arrow().to_pylist()
        by_path = {row["path"]: row for row in rows}
        if target not in by_path:
            raise ValueError("当前笔记尚未收录，请先同步索引")
        reference = by_path[target]
        lookup = {}
        for row in rows:
            for name in (row["path"], row["path"][:-3], Path(row["path"]).stem):
                lookup.setdefault(name, set()).add(row["path"])
        def linked_paths(row):
            result = set()
            for link in row["links"]:
                resolved = lookup.get(link, set())
                if len(resolved) == 1:
                    result.update(resolved)
            return result
        reference_links = linked_paths(reference)
        scored = []
        for row in self._filtered(rows, request):
            if row["path"] == target:
                continue
            links = linked_paths(row)
            direct = row["path"] in reference_links or target in links
            shared = reference_links.intersection(links)
            same_source = bool(reference["source_id"] and reference["source_id"] == row["source_id"])
            same_topic = bool(reference["topic"] and reference["topic"] == row["topic"])
            score = 8 * direct + 3 * len(shared) + 2 * same_source + same_topic
            if score:
                item = self._public(row, score)
                item["reasons"] = (["直接链接"] if direct else []) + ([f"共同链接 {len(shared)} 项"] if shared else []) + (["相同来源"] if same_source else []) + (["相同主题"] if same_topic else [])
                scored.append(item)
        scored.sort(key=lambda row: (-row["score"], row["path"]))
        limit = max(1, min(100, int(request.get("limit", 20))))
        return {"items": scored[:limit], "total": len(scored), "mode": "links"}

    def handle(self, request: dict) -> dict:
        if not isinstance(request, dict):
            raise ValueError("请求必须是 JSON 对象")
        op = request.get("op")
        if op == "status":
            return self.status()
        if op == "sync":
            semantic = request.get("semantic", True)
            if not isinstance(semantic, bool):
                raise ValueError("semantic 必须是布尔值")
            return self.sync(semantic=semantic)
        if op == "search":
            return self.search(request)
        if op == "related":
            return self.related(request)
        raise ValueError("未知操作；只支持 status、sync、search、related")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True)
    parser.add_argument("--db-dir", required=True)
    parser.add_argument("--model")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    index = VaultIndex(args.vault, args.db_dir, args.model, args.device)
    for line in sys.stdin:
        if not line.strip():
            continue
        request = {}
        try:
            request = json.loads(line)
            result = index.handle(request)
            response = {"id": request.get("id"), "ok": True, "result": result}
        except Exception as exc:
            response = {"id": request.get("id") if isinstance(request, dict) else None,
                        "ok": False, "error": str(exc)}
            print(f"索引操作失败：{type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        print(json.dumps(response, ensure_ascii=False, allow_nan=False), flush=True)
        if not args.serve:
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
