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

import azure.functions as func

version = "ZH 1.0.10"
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
            #connurl = os.getenv('AzureWebJobsStorage')
            connurl = "hello"
            logging.info('conn_str='+connurl +' version: ' + version)
            #acctname = "bgfastfunczipsa"
            #queue_client = QueueClient.from_connection_string(conn_str=connurl, queue_name=dest_queue_name,credential=DefaultAzureCredential())

            #queue_client = QueueClient.from_connection_string(conn_str=connect_str, queue_name=queue_name)

            #queue_client.send_message(os.path.basename(txt_file.name))
