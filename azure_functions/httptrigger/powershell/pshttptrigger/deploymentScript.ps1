

#https://learn.microsoft.com/en-us/azure/azure-functions/functions-core-tools-reference
#https://learn.microsoft.com/en-us/azure/azure-functions/

function Write-ColorOutput($ForegroundColor)
{
    # save the current color
    $fc = $host.UI.RawUI.ForegroundColor

    # set the new color
    $host.UI.RawUI.ForegroundColor = $ForegroundColor

    # output
    if ($args) {
        Write-Output $args
    }
    else {
        $input | Write-Output
    }

    # restore the original color
    $host.UI.RawUI.ForegroundColor = $fc
}

$json = Get-Content -Raw -Path .\local.settings.json | ConvertFrom-Json

$funcappname = $json.values.funcAppName

$res = func azure functionapp publish $funcappname --nozip --force
#Functions in psbgfastfa:
#    pshttptrigger - [httpTrigger]
#        Invoke url: https://{functionappname}.azurewebsites.net/api/pshttptrigger

# parse the result to get the invoke url
$funcappurl = $res | Select-String -Pattern "Invoke url:"
$funcappurl = $funcappurl -replace "Invoke url:",""
$funcappurl = $funcappurl.Trim() + "?name=$funcappname"
write-output $funcappurl
#make a rest call using the invoke url
$invokeres = Invoke-RestMethod -Method Post -Uri $funcappurl

# check the invokeres string for the existence of the $funcappname
if ($invokeres -match $funcappname) {
    Write-ColorOutput green "Function app $funcappname is working" 
} else {
    Write-ColorOutput red "Function app $funcappname is not working"
}


