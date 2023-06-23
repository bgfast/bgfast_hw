
$json = Get-Content -Raw -Path .\local.settings.json | ConvertFrom-Json

$resourceGroup = $json.values.resourceGroup

# webapp name
$deploymentName = $json.values.deploymentName
#$gitUserEmail = $json.values.gitUserEmail 
$gitUserName = $json.values.gitUserName 
$gitPassword = $json.values.gitPassword 
$subscriptionId = $json.values.selectedSubscription
#$ADOgitURI = $json.values.ADOgitURI  

mvn clean package

az login --use-device-code
$res = az account set --subscription "$subscriptionId"
Write-Host "az webapp deployment user set --user-name $gitUserName --password $gitPassword"
$res = az webapp deployment user set --user-name $gitUserName --password $gitPassword
Write-Host "az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path .\target\azure-sql-java-samples-1.war --type war"
az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path .\target\azure-sql-java-samples-1.war --type war
#az webapp deploy --resource-group $resourceGroup --name $deploymentName --src-path C:\code\db-azure-sql-java\target\azure-sql-java-samples-1.war
