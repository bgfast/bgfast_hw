
$json = Get-Content -Raw -Path .\local.settings.json | ConvertFrom-Json

$resourceGroup = $json.values.resourceGroup

# webapp name
$deploymentName = $json.values.deploymentName
$gitUserEmail = $json.values.gitUserEmail 
$gitUserName = $json.values.gitUserName 
$gitPassword = $json.values.gitPassword 
$subscriptionId = $json.values.selectedSubscription
$ADOgitURI = $json.values.ADOgitURI  

mvn clean package

if (Test-Path ./.git/config.lock) {
    Remove-Item -Force ./.git/config.lock
}
#Write-Host "Publishing sample app.. (this might take a minute or two)"
#Write-Host "git init"
#git init
#Write-Host "git config user.email $gitUserEmail"
#git config user.email "$gitUserEmail"
#Write-Host "git config user.name $gitUserName"
#git config user.name "$gitUserName"
#Write-Host "git add -A"
#git add -A
#Write-Host "git config http.postBuffer 52488000"
#git config http.postBuffer 52488000
#Write-Host "git commit -m 'Initial commit'"
#git commit -m "Initial commit"

# are the git commands needed if we run the webapp deploy command?
#az login 
$res = az account set --subscription "$subscriptionId"
Write-Host "az webapp deployment user set --user-name $gitUserName --password $gitPassword"
$res = az webapp deployment user set --user-name $gitUserName --password $gitPassword
Write-Host "az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path .\target\azure-sql-java-samples-1.war"
$res = az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path .\target\azure-sql-java-samples-1.war
#az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path C:\code\db-azure-sql-java\target\azure-sql-java-samples-1.war

#Write-Host "git remote rm azwebapp "
#git remote rm azwebapp 
#Write-Host "git remote add azwebapp $ADOgitURI"
#git remote add azwebapp $ADOgitURI
#Write-Host "git push -v --force azwebapp master"
#git push -v --force azwebapp master
