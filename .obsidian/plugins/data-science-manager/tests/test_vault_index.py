"""纯解析检查可运行 ParserTests；完整测试需在允许本地回环的环境运行。"""

from __future__ import annotations

import hashlib
import gc
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


sys.dont_write_bytecode = True
SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "vault_index.py"
spec = importlib.util.spec_from_file_location("data_science_vault_index", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
VaultIndex = module.VaultIndex


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp_parent = Path(__file__).resolve().parent / "_test_work"
        self.temp_parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="case-", dir=self.temp_parent)
        self.fixture = Path(self.temporary.name).resolve()
        self.assertTrue(self.fixture.is_relative_to(self.temp_parent.resolve()))
        self.vault = self.fixture / "vault"
        self.vault.mkdir()
        self.index = VaultIndex(self.vault, self.vault / ".vault-index" / "lancedb")

    def tearDown(self):
        # Windows 上仅清理由本测试建立、已核对归属的临时目录。
        self.assertEqual(self.fixture.parent, self.temp_parent.resolve())
        self.assertTrue(self.fixture.name.startswith("case-"))
        self.index._db = None
        gc.collect()
        self.temporary.cleanup()

    def note(self, relative, title="最小二乘与梯度", kind="concept", body="最小二乘 Gradient descent", **fields):
        metadata = {"title": title, "tags": [kind], "status": "not-started", **fields}
        lines = [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in metadata.items()]
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + "\n".join(lines) + "\n---\n\n" + body + "\n", encoding="utf-8")
        return path


class ParserTests(Fixture):
    def test_inline_tags_and_topic_fallback(self):
        path = self.note("04 - 统计学习/概念/回归.md", source_id="DS001")
        row = self.index.parse_note(path)
        self.assertEqual(row["kind"], "concept")
        self.assertEqual(row["tags"], ["concept"])
        self.assertEqual(row["topic"], "statistical-learning")
        self.assertEqual(row["topic_label"], "统计学习")
        self.assertEqual(row["source_id"], "DS001")

    def test_same_basenames_have_distinct_relative_paths(self):
        self.note("04 - 统计学习/概念/同名.md")
        self.note("05 - 概率模型与推断/概念/同名.md")
        self.assertEqual(len(self.index.scan()), 2)

    def test_excluded_directories_and_tags(self):
        self.note("模板/概念模板.md")
        self.note("附件/伪笔记.md")
        self.note(".obsidian/伪笔记.md")
        self.note("04 - 统计学习/.hidden/伪笔记.md")
        self.note("04 - 统计学习/导航.md", kind="hub")
        self.note("00 - 首页/教材归档/DS001.md", kind="source")
        rows = self.index.scan()
        self.assertEqual(list(rows), ["00 - 首页/教材归档/DS001.md"])

    def test_database_and_note_paths_cannot_escape_vault(self):
        outside = self.fixture / "outside.md"
        outside.write_text("保留", encoding="utf-8")
        with self.assertRaises(ValueError):
            VaultIndex(self.vault, self.fixture / "other-index")
        with self.assertRaises(ValueError):
            VaultIndex(self.vault, self.vault)
        with self.assertRaises(ValueError):
            self.index.checked_note_path("../outside.md")
        self.assertEqual(outside.read_text(encoding="utf-8"), "保留")

    def test_python_yaml_object_is_rejected_without_execution(self):
        marker = self.fixture / "yaml-executed.txt"
        payload = f"__import__('pathlib').Path({str(marker)!r}).touch()"
        path = self.vault / "04 - 统计学习/概念/危险元数据.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\ntags: [concept]\ntitle: !!python/object/apply:builtins.eval\n- "
                        + json.dumps(payload) + "\n---\n正文", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.index.scan()
        self.assertFalse(marker.exists())

    def test_status_does_not_import_or_create_database(self):
        state = self.index.status()
        self.assertFalse(state["exists"])
        self.assertEqual(state["total"], 0)
        self.assertFalse(self.index.db_dir.exists())

    def test_escaped_wikilink_alias_in_markdown_table(self):
        path = self.note("00 - 首页/教材归档/DS001.md", kind="source",
                         body="| 原题 | 笔记 |\n| --- | --- |\n| 2.1 | [[04 - 统计学习/概念/回归\\|回归]] |")
        row = self.index.parse_note(path)
        self.assertEqual(row["links"], ["04 - 统计学习/概念/回归"])


class LanceIntegrationTests(Fixture):
    def setup_notes(self):
        first = self.note("04 - 统计学习/概念/同名.md", source_id="DS001")
        second = self.note("05 - 概率模型与推断/概念/同名.md", title="贝叶斯推断", body="Bayesian inference", source_id="DS002")
        return first, second

    def test_incremental_sync_and_same_basename(self):
        first, second = self.setup_notes()
        original = {path: path.read_bytes() for path in (first, second)}
        result = self.index.sync(semantic=False)
        self.assertEqual((result["added"], result["total"]), (2, 2))
        self.assertFalse(result["semantic_ready"])
        self.assertEqual(self.index.sync(semantic=False)["unchanged"], 2)
        self.assertEqual(original, {path: path.read_bytes() for path in original})
        first.write_text(first.read_text(encoding="utf-8") + "\n新内容\n", encoding="utf-8")
        result = self.index.sync(semantic=False)
        self.assertEqual((result["updated"], result["unchanged"]), (1, 1))
        rows = self.index._table().to_arrow().to_pylist()
        self.assertEqual(len({row["path"] for row in rows}), 2)
        self.assertTrue(all(row["vector"] is None for row in rows))

    def test_keyword_chinese_english_and_metadata_filters(self):
        self.setup_notes()
        self.index.sync(semantic=False)
        chinese = self.index.search({"query": "最小二乘", "kind": "concept"})
        english = self.index.search({"query": "GRADIENT"})
        self.assertEqual(chinese["total"], 1)
        self.assertEqual(english["total"], 1)
        self.assertEqual(chinese["items"][0]["path"], english["items"][0]["path"])
        self.assertEqual(self.index.search({"query": "", "source_id": "DS002"})["total"], 1)
        self.assertEqual(self.index.search({"query": "", "status": "completed"})["total"], 0)
        self.assertEqual(self.index.search({"query": "", "source_id": "DS001' OR 1=1"})["total"], 0)

    def test_delete_and_rename_change_only_index_records(self):
        first, second = self.setup_notes()
        self.index.sync(semantic=False)
        second_before = second.read_bytes()
        renamed = first.with_name("新文件名.md")
        first.rename(renamed)
        result = self.index.sync(semantic=False)
        self.assertEqual((result["added"], result["deleted"], result["total"]), (1, 1, 2))
        self.assertEqual(second.read_bytes(), second_before)
        renamed.unlink()
        result = self.index.sync(semantic=False)
        self.assertEqual((result["deleted"], result["total"]), (1, 1))
        self.assertTrue(second.exists())
        self.assertEqual(second.read_bytes(), second_before)

    def test_safe_yaml_failure_does_not_delete_existing_index(self):
        first, _ = self.setup_notes()
        self.index.sync(semantic=False)
        first.write_text("---\ntags: [concept]\ntitle: !!python/object:builtins.list {}\n---\n正文", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.index.sync(semantic=False)
        self.assertEqual(self.index.status()["total"], 2)
        self.assertEqual(self.index._table().count_rows(), 2)

    def test_existing_unowned_database_directory_is_preserved(self):
        sentinel = self.index.db_dir / "personal-content.txt"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_text("不得覆盖", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.index.sync(semantic=False)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "不得覆盖")

    def test_relation_search_uses_actual_links(self):
        concept = self.note("04 - 统计学习/概念/回归.md")
        self.note("04 - 统计学习/习题/习题 ML001 - 回归.md", kind="exercise",
                  body="| 原题 | 笔记 |\n| --- | --- |\n| 2.1 | [[04 - 统计学习/概念/回归\\|概念]] |",
                  source_id="DS001", source_exercise="2.1")
        self.index.sync(semantic=False)
        result = self.index.related({"path": concept.relative_to(self.vault).as_posix(), "kind": "exercise"})
        self.assertEqual(result["total"], 1)
        self.assertIn("直接链接", result["items"][0]["reasons"])


if __name__ == "__main__":
    unittest.main()
