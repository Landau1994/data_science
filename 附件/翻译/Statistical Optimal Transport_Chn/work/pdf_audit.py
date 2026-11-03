"""全书流程兼容入口；当前交付不再使用第1章生成器。"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('audit_full_pdf.py')), run_name="__main__")
