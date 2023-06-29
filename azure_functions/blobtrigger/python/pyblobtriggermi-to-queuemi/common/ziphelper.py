import azure.functions as func
from azure.storage.blob import BlobServiceClient
from io import BytesIO
import json
import logging
import os
import sys
import zipfile
from azure.storage.queue import QueueClient
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient

import azure.functions as func

version = "ZH pyblobtriggermi-to-queuemi 1.0.14"

def process_zip_file(myblob, dest_container_client, dest_queue_client):
    logging.info('Starting process_zip_file. version: ' + version)
    # Read the contents of the zip file
    data = myblob.read()
    zip_file = zipfile.ZipFile(BytesIO(data))

    for file in zip_file.namelist():
        with zip_file.open(file) as txt_file:
            logging.info('Uploading file to blob '+txt_file.name+' version: ' + version)
            # only get the file name - ignore the path from inside the zip file
            blob_client = dest_container_client.get_blob_client(os.path.basename(txt_file.name))
            blob_client.upload_blob(txt_file.read(), overwrite=True)
            dest_queue_name = os.getenv('GENAI_DEST_QUEUE_NAME')
            sa_account_url1 = os.getenv('GENAI_SA_ACCOUNT_URL')
            default_credential = DefaultAzureCredential()

            #sa_account_url = "https://bgfastfunczipsa.blob.core.windows.net"
            queue_url = sa_account_url1 + "/" + dest_queue_name
            queue_service_client = QueueServiceClient(sa_account_url1, credential=default_credential)
            #queue_client = queue_service_client.from_queue_url("https://bgfastfunczipsa.queue.core.windows.net/azure-webjobs-blobtrigger-bgfast-funczip-fa", credential=default_credential)
            queue_client = queue_service_client.from_queue_url(queue_url, credential=default_credential)
            queue_client.send_message(os.path.basename(txt_file.name))
