# wf-gate.ps1 — 工作流门禁检查
# 生成步骤前必须运行此脚本。条件不满足则拒绝继续。

param(
    [string]$WikiRoot = (Get-Item (Split-Path $PSScriptRoot -Parent)).FullName,
    [string]$Slug = "",
    [switch]$Quiet
)

$pendingDir = Join-Path $WikiRoot "_待审核"
function Write-Msg($M) { if (-not $Quiet) { Write-Host $M } }

# 检查1: _pending/ 是否存在且有文件
if (-not (Test-Path $pendingDir)) {
    if (-not $Quiet) {
        Write-Host "--- WF-GATE: BLOCKED ---" -ForegroundColor Red
        Write-Host "_待审核/ directory does not exist!" -ForegroundColor Red
        Write-Host "You must write the analysis report to _pending/ first." -ForegroundColor Yellow
        Write-Host "Then wait for the user to approve before generating wiki pages." -ForegroundColor Yellow
    }
    exit 1
}

$pendingFiles = Get-ChildItem -Path $pendingDir -Filter "*.md"
if ($pendingFiles.Count -eq 0) {
    if (-not $Quiet) {
        Write-Host "--- WF-GATE: BLOCKED ---" -ForegroundColor Red
        Write-Host "_待审核/ is empty! No analysis report found." -ForegroundColor Red
        Write-Host "You must write the analysis report to _pending/ first." -ForegroundColor Yellow
    }
    exit 1
}

# 检查2: 是否所有报告都已处理（含✅标记）
$hasUnprocessed = $false
foreach ($f in $pendingFiles) {
    $line = Get-Content -Encoding UTF8 $f -First 5
    if (("$line" -join "
") -notmatch "u{2705} 已处理") {
        $hasUnprocessed = $true
    }
}

if (-not $hasUnprocessed) {
    if (-not $Quiet) {
        Write-Host "--- WF-GATE: WARNING ---" -ForegroundColor Yellow
        Write-Host "All reports in _pending/ are already processed (marked with checkmark)." -ForegroundColor Yellow
        Write-Host "Confirming this is a new operation, not a duplicate." -ForegroundColor Yellow
    }
    exit 1
}

# 检查3: 如果指定了slug，精确匹配
if ($Slug -ne "") {
    $matched = $false
    foreach ($f in $pendingFiles) {
        if ($f.Name -like "*$Slug*") { $matched = $true; break }
    }
    if (-not $matched) {
        if (-not $Quiet) {
            Write-Host "--- WF-GATE: BLOCKED ---" -ForegroundColor Red
            Write-Host "No matching report found for slug: $Slug" -ForegroundColor Red
        }
        exit 1
    }
}

# 放行
if (-not $Quiet) {
    Write-Host "--- WF-GATE: PASS ---" -ForegroundColor Green
    Write-Host "Pending reports: $($pendingFiles.Count)" -ForegroundColor Green
    foreach ($f in $pendingFiles) {
        Write-Host "  $($f.Name)" -ForegroundColor Gray
    }
    Write-Host "Make sure the user has approved before generating." -ForegroundColor Yellow
}
exit 0
