<#
Simple helper to run the example spider on Windows.
Usage:
  Open PowerShell, activate your virtualenv, then:
    .\run_spider.ps1
#>

$scriptPath = Join-Path -Path $PSScriptRoot -ChildPath 'Distributed Web Crawler\my_spider.py'
if (-Not (Test-Path $scriptPath)) {
    Write-Error "Spider script not found: $scriptPath"
    exit 1
}

Write-Output "Running spider: $scriptPath"
python $scriptPath
