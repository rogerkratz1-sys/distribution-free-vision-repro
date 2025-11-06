# verify-environment.ps1
# Lightweight smoke test for Windows PowerShell
Write-Output "PowerShell version: $($PSVersionTable.PSVersion)"
Write-Output "Current directory: $(Get-Location)"

# Check Python presence and version
$pythonCmd = "python"
try {
    $pyver = & $pythonCmd --version 2>&1
    if ($LASTEXITCODE -ne 0) { throw "python not found or failed" }
    Write-Output "Python version: $pyver"
} catch {
    Write-Error "Python not found on PATH. Install Python or adjust PATH."
    exit 127
}

# Sanity-check: run a short dry-run of a lightweight script if present
$smokeScripts = @(".\plot_delta_vs_k.py", ".\scripts\test_table_D_checks.py")
$found = $false
foreach ($s in $smokeScripts) {
    if (Test-Path $s) {
        Write-Output "Running smoke script: $s"
        & $pythonCmd $s --help 2>&1 | ForEach-Object { Write-Output $_ }
        $found = $true
    }
}

if (-not $found) {
    Write-Output "No listed smoke scripts found; listing tracked Python files instead:"
    git ls-files -- '*.py' | ForEach-Object { Write-Output " - $_" }
}

Write-Output "Smoke test completed. If no errors were reported, exit code 0 is returned."
exit 0
