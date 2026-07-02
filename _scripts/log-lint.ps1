# log-lint.ps1 — check log.md completeness vs raw/ files
# Run after each learning session to catch missing log entries
param([string]$WikiRoot = (Get-Item (Split-Path $PSScriptRoot -Parent)).FullName, [switch]$FixDates)

$logPath = Join-Path $WikiRoot "日志.md"
$rawDir  = Join-Path $WikiRoot "原始素材"
$issuesFound = $false

function Write-Issue($Type, $Message) {
    $script:issuesFound = $true
    Write-Host "[$Type] $Message" -ForegroundColor @{ERROR="Red"; WARNING="Yellow"}[$Type]
}

function Normalize-Name($n) {
    # Strip .md, normalize whitespace and quotes
    $n = $n -replace "\.md$", ""
    $n = $n -replace "[\u201c\u201d\u2018\u2019]", "\u0022"  # normalize quotes
    $n = $n -replace "\s+", " "
    $n.ToLower()
}

Write-Host "--- Step 1: Scan raw/ ---" -ForegroundColor Magenta
$rawFiles = Get-ChildItem -Recurse -File $rawDir -Include "*.md" | Where-Object {
    $_.FullName -notmatch "assets" -and $_.FullName -notmatch "JHZ_Thesis"
}
Write-Host "  Found $($rawFiles.Count) markdown files in raw/" -ForegroundColor Gray

Write-Host "--- Step 2: Parse log.md ---" -ForegroundColor Magenta
$logFileRefs = @{}
$logContent = Get-Content -Encoding UTF8 $logPath
$currentDate = $null
$bt = [char]96
foreach ($line in $logContent) {
    if ($line -match "^## \[(\d{4}-\d{2}-\d{2})\]") { $currentDate = $Matches[1] }
    $i = 0
    while ($i -lt $line.Length) {
        $s = $line.IndexOf($bt, $i)
        if ($s -lt 0) { break }
        $e = $line.IndexOf($bt, $s + 1)
        if ($e -lt 0) { break }
        $path = $line.Substring($s + 1, $e - $s - 1)
        $i = $e + 1
        if ($path -match "[\\\\/]") {
            $name = Split-Path $path -Leaf
            $normal = Normalize-Name $name
            if (-not $logFileRefs.ContainsKey($normal)) { $logFileRefs[$normal] = @() }
            $logFileRefs[$normal] += @{ Date = $currentDate; Name = $name; Path = $path }
        }
    }
}
Write-Host "  Parsed $($logFileRefs.Count) unique file refs from log.md" -ForegroundColor Gray

Write-Host "--- Step 3: Compare raw vs log ---" -ForegroundColor Magenta
$missingInLog = @()
$dateIssues = @()
foreach ($f in $rawFiles) {
    $norm = Normalize-Name $f.Name
    # Try exact match first
    if ($logFileRefs.ContainsKey($norm)) {
        if ($FixDates) {
            $fileDate = $f.LastWriteTime.ToString("yyyy-MM-dd")
            foreach ($ref in $logFileRefs[$norm]) {
                if ($ref.Date) {
                    $diff = [math]::Abs(([datetime]$fileDate - [datetime]$ref.Date).TotalDays)
                    if ($diff -gt 2) { $dateIssues += @{Name=$f.Name; FileDate=$fileDate; LogDate=$ref.Date; Diff=$diff} }
                }
            }
        }
        continue
    }
    # Try fuzzy match with ... truncation
    $found = $false
    foreach ($logNorm in $logFileRefs.Keys) {
        if ($logNorm -match "\.\.\.") {
            $parts = $logNorm -split "\.\.\."
            $prefix = $parts[0]
            $suffix = if ($parts.Count -gt 1) { $parts[-1] } else { "" }
            if ($norm -like "$prefix*$suffix") { $found = $true; break }
        }
    }
    if (-not $found) { $missingInLog += $f }
}

if ($missingInLog.Count -gt 0) {
    Write-Issue "ERROR" "Missing in log.md: $($missingInLog.Count) files (after fuzzy match)"
    $missingInLog | Sort-Object LastWriteTime | ForEach-Object {
        Write-Host "  $($_.LastWriteTime.ToString("MM-dd HH:mm"))  $($_.Name)" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "  Tip: Check if these are genuinely missing or need log entry update" -ForegroundColor Cyan
} else {
    Write-Host "  PASS: all $($rawFiles.Count) raw files match log.md records" -ForegroundColor Green
}

if ($dateIssues.Count -gt 0) {
    Write-Issue "WARNING" "Date inconsistencies: $($dateIssues.Count) files"
    $dateIssues | ForEach-Object {
        Write-Host "  $($_.Name): raw=$($_.FileDate) vs log=$($_.LogDate) (diff $($_.Diff)d)" -ForegroundColor Yellow
    }
}

Write-Host "========================================" -ForegroundColor Magenta
if ($issuesFound) { Write-Host "FAIL: issues found - check above" -ForegroundColor Yellow; exit 1 }
else { Write-Host "PASS: all checks clean" -ForegroundColor Green; exit 0 }
