"""从原PDF裁出两幅无编号习题图，保留原标注与矢量内容。"""
from pathlib import Path
from copy import copy
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parent.parent
source = root.parent.parent / 'books/Santambrogio 2015 Optiomal Transport For Applied Mathematicians.pdf'
pdf = PdfReader(source)
for page_number, name, box in [
    (352, 'ex28-network', (.75,.195,.88,.278)),
    (356, 'ex57-points', (.24,.605,.38,.692)),
]:
    page = copy(pdf.pages[page_number-1])
    width, height = float(page.mediabox.width), float(page.mediabox.height)
    x0, top0, x1, top1 = box
    page.cropbox.lower_left = (x0*width, (1-top1)*height)
    page.cropbox.upper_right = (x1*width, (1-top0)*height)
    page.mediabox = copy(page.cropbox)
    writer = PdfWriter()
    writer.add_page(page)
    target = root / 'assets' / (name+'.pdf')
    with target.open('wb') as stream:
        writer.write(stream)
    print(name, page_number, box)
