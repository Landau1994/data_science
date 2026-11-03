"""在本目录构建当前已译范围，保留编译日志，并更新正式 PDF。"""
from pathlib import Path
import hashlib
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
STEM = "Optimal Transport for Applied Mathematicians_Chn"
WORK = ROOT / "work"
SOURCE = ROOT.parent.parent / "books" / "Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf"


def run(args, name):
    result = subprocess.run(args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (WORK / name).write_bytes(result.stdout)
    if result.returncode:
        raise SystemExit(f"构建未通过，请查看 work/{name}")


def main():
    WORK.mkdir(exist_ok=True)
    before = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    args = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-output-directory=work", STEM + ".tex"]
    run(args, "build-xelatex-1.log")
    run(["bibtex", "work/" + STEM], "build-bibtex.log")
    run(args, "build-xelatex-2.log")
    run(args, "build-xelatex-3.log")
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != before:
        raise SystemExit("原书校验值发生变化，停止交付。")
    shutil.copy2(WORK / (STEM + ".pdf"), ROOT / (STEM + ".pdf"))
    print("已生成当前范围 PDF；内容核对、视觉和链接审计须另行执行。")


if __name__ == "__main__":
    main()
