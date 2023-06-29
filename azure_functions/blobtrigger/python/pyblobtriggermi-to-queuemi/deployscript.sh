# set the subscription id for the deployment

# to do: get info from local.settings.json
az account set --subscription 000000000-0000-0000-0000-000000000000
func azure functionapp publish funcappname --force --python