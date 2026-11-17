import pathlib,sys
b=pathlib.Path(r'E:/project/math/data_science/附件/翻译/Statistical Inference_Chn')
p=b/'sections-tex/09-05.tex';t=p.read_text(encoding='utf-8').replace('$(\\mu_X,\\mu_Y,\\sigma_X^2,\\sigma_Y^2,\\rho)$','$(\\mu_X,\\allowbreak\\mu_Y,\\allowbreak\\sigma_X^2,\\allowbreak\\sigma_Y^2,\\allowbreak\\rho)$');p.write_text(t,encoding='utf-8')
