$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    New-Item -ItemType Directory -Path 'work' -Force | Out-Null
    1..3 | ForEach-Object {
        & xelatex -interaction=nonstopmode -halt-on-error -output-directory=work 'Statistical Inference_Chn.tex'
        if ($LASTEXITCODE -ne 0) { throw 'LaTeX 构建失败，请检查 work 中的日志。' }
    }
    $indexStable = $false
    foreach ($indexPass in 1..3) {
        $beforeIndex = (Get-FileHash -LiteralPath 'backmatter\04-index.tex' -Algorithm SHA256).Hash
        & python -X utf8 'work\build-index.py'
        if ($LASTEXITCODE -ne 0) { throw '索引生成失败。' }
        $afterIndex = (Get-FileHash -LiteralPath 'backmatter\04-index.tex' -Algorithm SHA256).Hash
        if ($beforeIndex -eq $afterIndex) { $indexStable = $true; break }
        1..2 | ForEach-Object {
            & xelatex -interaction=nonstopmode -halt-on-error -output-directory=work 'Statistical Inference_Chn.tex'
            if ($LASTEXITCODE -ne 0) { throw '索引更新后的 LaTeX 构建失败。' }
        }
    }
    if (-not $indexStable) { throw '索引页码尚未稳定，请检查 work。' }
    & makeindex -o 'work\Statistical Inference_Chn.ind' -t 'work\Statistical Inference_Chn.ilg' 'work\Statistical Inference_Chn.idx'
    if ($LASTEXITCODE -ne 0) { throw '标准索引语法检查失败。' }
    Copy-Item -LiteralPath 'work\Statistical Inference_Chn.pdf' -Destination 'Statistical Inference_Chn.pdf' -Force
} finally {
    Pop-Location
}
