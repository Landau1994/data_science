"""Compatibility entry for the final full-book audit.

The former chapter-1 / 94-page audit has been retired.  This entry now delegates
all arguments to audit-full.py, which follows the real MAIN input graph and the
complete 376-page source.  It never compiles or changes TeX.  Use
--write-manifest explicitly to update the manifest after a successful audit.
"""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("audit-full.py")), run_name="__main__")
