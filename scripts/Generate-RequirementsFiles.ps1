pip freeze > env/pip_config/requirements.txt
conda list --export > env/conda_config/requirements.txt

$ErrorActionPreference = "Stop"

# Check if pip and conda are installed and accessible from PATH.
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Error "pip is not available. Is it installed correctly?"
    exit 1
}

if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
    Write-Error "conda is not available. Is it installed correctly?"
    exit 1
}


# Check env directories exist, else create them.
if (-not (Test-Path -Path env/pip_config)) {
    New-Item -Path env/pip_config -ItemType Directory
}

if (-not (Test-Path -Path env/conda_config)) {
    New-Item -Path env/conda_config -ItemType Directory
}

# Generate pip requirements.txt
pip freeze > env/pip_config/requirements.txt

# Generate conda requirements.txt
conda list --export > env/conda_config/requirements.txt

Write-Output "Requirement files generated successfully!"