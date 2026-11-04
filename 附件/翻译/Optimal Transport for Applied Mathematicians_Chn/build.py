"""构建中文全译稿及动态索引，保留日志，收敛后更新交付 PDF。"""
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
    def snapshot():
        return tuple((WORK / (STEM + suffix)).read_bytes() for suffix in (".aux", ".toc", ".idx"))
    for number in range(2, 7):
        before_pass = snapshot()
        run(["makeindex", "-s", "work/translated-index.ist", "-o", "work/" + STEM + ".ind",
             "-t", "work/" + STEM + ".ilg", "work/" + STEM + ".idx"], f"build-makeindex-{number}.log")
        run(args, f"build-xelatex-{number}.log")
        if number >= 3 and snapshot() == before_pass:
            break
    else:
        raise SystemExit("页码、索引或引用在六遍后仍未稳定，请检查日志。")
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != before:
        raise SystemExit("原书校验值发生变化，停止交付。")
    shutil.copy2(WORK / (STEM + ".pdf"), ROOT / (STEM + ".pdf"))
    print(f"已生成全译稿 PDF（{number}遍XeLaTeX，BibTeX及动态索引）；视觉和链接审计另行执行。")


if __name__ == "__main__":
    main()
