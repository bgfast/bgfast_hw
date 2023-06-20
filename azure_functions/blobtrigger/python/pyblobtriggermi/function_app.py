import azure.functions as func
import logging
import os
from azure.storage.blob import BlobServiceClient
from azure.storage.queue import QueueServiceClient
from azure.identity import DefaultAzureCredential

from common import ziphelper

app = func.FunctionApp()

version = "FA 1.0.10"

@app.function_name(name="HttpWebpageTrigger")
@app.route(route="webpage")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request. version: ' + version)

    name = req.params.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        logging.info('Python HTTP trigger function processed a request. no name')
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

#https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python
#https://learn.microsoft.com/en-us/azure/storage/common/storage-samples-python?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json#blob-samples
#https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference?tabs=blob#connecting-to-host-storage-with-an-identity
#https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cin-process&pivots=programming-language-python#decorators
#https://techcommunity.microsoft.com/t5/apps-on-azure-blog/use-managed-identity-instead-of-azurewebjobsstorage-to-connect-a/ba-p/3657606
#https://github.com/cloud-custodian/cloud-custodian/blob/631c3a9df00b9b6c3143774652bf4e1e848a9b6b/tools/c7n_azure/c7n_azure/resources/storage.py#L483
@app.function_name(name="BlobTrigger1")
@app.blob_trigger(arg_name="myblob", connection="AzureWebJobsStorage", path="%GENAI_SRC_CONTAINER_NAME%")
def test_function(myblob: func.InputStream):
    logging.info('Python blob trigger function processed a request. version: ' + version)

    account_url = "https://bgfastfunczipsa.blob.core.windows.net"
    default_credential = DefaultAzureCredential()

    blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    queue_service_client = QueueServiceClient(account_url, credential=default_credential)

    dest_container_name = os.getenv('GENAI_DEST_CONTAINER_NAME')
    dest_queue_name = os.getenv('GENAI_DEST_QUEUE_NAME')
    logging.info('dest container:' + dest_container_name+' version: ' + version)
    logging.info('dest queue:' + dest_queue_name+' version: ' + version)

    if myblob is None:
        #logger.debug("{fv} myblob is None. getting func.InputStream()")
        myblob = func.InputStream()
    #logging.info(f"Python blob trigger function processed blob \n"
    #             f"Name: {myblob.name}\n"
    #             f"Blob Size: {myblob.length} bytes")
    dest_container_client = blob_service_client.get_container_client(dest_container_name)
    dest_queue_client = queue_service_client.get_queue_client(dest_queue_name)
    
    ziphelper.process_zip_file(myblob, dest_container_client, dest_queue_client)