$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$taskPrefix = $taskRoot.TrimEnd('\') + '\'
$taskWork = Join-Path $taskRoot 'work'
$taskRemoved = [System.Collections.Generic.List[object]]::new()

function Test-TaskPath([string]$targetPath) {
    $resolvedPath = (Resolve-Path -LiteralPath $targetPath).Path
    if (-not $resolvedPath.StartsWith($taskPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing cleanup outside translation output: $resolvedPath"
    }
    return $resolvedPath
}

function Remove-TaskFile([System.IO.FileInfo]$taskFile) {
    $checkedPath = Test-TaskPath $taskFile.FullName
    $taskRemoved.Add([ordered]@{path=$checkedPath.Substring($taskPrefix.Length); bytes=$taskFile.Length})
    Remove-Item -LiteralPath $checkedPath -Force
}

# These folders contain only task-generated extraction/render/checking copies.
# Canonical TeX, PDF, bibliography, assets and reports are outside these folders.
foreach ($taskRelative in @('work\full-temp','work\rendered','work\full-static-scope','work\static-scope','split-pdf')) {
    $taskDir = Join-Path $taskRoot $taskRelative
    if (Test-Path -LiteralPath $taskDir) {
        $checkedDir = Test-TaskPath $taskDir
        $taskFiles = @(Get-ChildItem -LiteralPath $checkedDir -File -Recurse)
        if (@($taskFiles | Where-Object Extension -eq '.log').Count -gt 0) {
            throw "A compilation log must be retained: $checkedDir"
        }
        foreach ($taskFile in $taskFiles) {
            $taskRemoved.Add([ordered]@{path=$taskFile.FullName.Substring($taskPrefix.Length); bytes=$taskFile.Length})
        }
        # The resolved absolute directory was checked above before recursion.
        Remove-Item -LiteralPath $checkedDir -Recurse -Force
    }
}

$taskAux = @('.aux','.out','.toc','.xdv','.idx','.ind','.ilg','.bbl','.blg','.fls','.fdb_latexmk','.nav','.snm','.vrb')
foreach ($taskDir in @($taskWork, (Join-Path $taskWork 'full-build'))) {
    $checkedDir = Test-TaskPath $taskDir
    foreach ($taskFile in @(Get-ChildItem -LiteralPath $checkedDir -File)) {
        if ($taskFile.Extension -in $taskAux -or $taskFile.Name -like '*.synctex.gz' -or $taskFile.Extension -eq '.txt' -or ($taskDir -eq $taskWork -and $taskFile.Extension -eq '.png')) {
            Remove-TaskFile $taskFile
        }
    }
}
foreach ($taskName in @('combined-for-static.tex','full-combined-for-static.tex','full-main-draft.tex','full-output-page-digests-previous.json','probe.pdf')) {
    $taskPath = Join-Path $taskWork $taskName
    if (Test-Path -LiteralPath $taskPath) { Remove-TaskFile (Get-Item -LiteralPath $taskPath) }
}
$taskBytes = [long]0
foreach ($taskEntry in $taskRemoved) { $taskBytes += [long]$taskEntry['bytes'] }
$taskReport = [ordered]@{
    date='2026-11-03'
    scope=$taskRoot
    removed_files=$taskRemoved.Count
    removed_bytes=$taskBytes
    preserved='Original PDF; delivered and historical compiled PDFs; canonical TeX; bibliography; assets; all .log files; source ledgers; audit/review reports; build scripts'
    removed=$taskRemoved
}
$taskReport | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $taskWork 'cleanup-report.json') -Encoding utf8
$taskMB = [Math]::Round($taskBytes / 1MB, 2)
@"
# 本次译制临时文件清理

2026-11-03，按用户要求，已清理本次任务生成的 $($taskRemoved.Count) 个临时文件，共 $taskBytes 字节（约 $taskMB MiB）。每个删除目标均先核对解析后的绝对路径，全部位于本译稿目录内。

- 已清理：原书拆分副本、原页与译稿预览PNG、提取文本、索引定位暂存副本、完整展开的静态检查副本、构建标准输出文本及编译辅助文件。
- 保留：原始PDF、正式235页PDF、LaTeX主稿与全部分节稿、书目、正式图件、所有编译.log、来源与复核报告、图像哈希、编号/链接数据和可重复构建脚本。历史已编译PDF作为试译/构建产物保留，不作为正式入口。
- 删除文件的相对路径与大小见同目录cleanup-report.json。未触及译稿目录外文件；没有Git分支、提交、推送或发布操作。

再次构建或查看预览时，相应工具会重新生成必要辅助文件。
"@ | Set-Content -LiteralPath (Join-Path $taskWork 'cleanup-report.md') -Encoding utf8
Write-Output "Cleaned $($taskRemoved.Count) task-temporary files; $taskMB MiB. Canonical outputs and logs retained."
