Write-Output "#### Update from GitHub ####"
git pull origin main

Write-Output "#### Add and commit ####"
$commitMessage = "Salvo em $(Get-Date -Format 'dd-MM-yyyy HH:mm:ss')"
git add .
git commit -m $commitMessage

Write-Output "#### Update GitHub ####"
git push origin main