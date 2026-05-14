$packDir = ".\hardcore_project\pack"
$clientDir = ".\client_main\overrides"

Write-Host "Deploying Packwiz project to client_main..."

# 1. Clean the client's KubeJS folder to avoid orphaned scripts
if (Test-Path "$clientDir\kubejs") {
    Write-Host "Cleaning old KubeJS scripts..."
    Remove-Item -Recurse -Force "$clientDir\kubejs"
}

# 2. Copy the new KubeJS folder
Write-Host "Copying new KubeJS scripts..."
Copy-Item -Recurse -Force "$packDir\kubejs" "$clientDir\"

# 3. Copy configs and defaultconfigs
if (Test-Path "$clientDir\config") { Remove-Item -Recurse -Force "$clientDir\config" }
Copy-Item -Recurse -Force "$packDir\config" "$clientDir\"

if (Test-Path "$packDir\defaultconfigs") {
    if (Test-Path "$clientDir\defaultconfigs") { Remove-Item -Recurse -Force "$clientDir\defaultconfigs" }
    Copy-Item -Recurse -Force "$packDir\defaultconfigs" "$clientDir\"
}

Write-Host "Deployment complete! You can now launch the game."
Write-Host "Note: For mods, we highly recommend using the Packwiz Installer Bootstrapper!"
