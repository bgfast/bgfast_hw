import azure.functions as func
from azure.storage.blob import BlobServiceClient
from io import BytesIO
import json
import logging
import os
import sys
import zipfile
from azure.storage.queue import QueueClient

import azure.functions as func

#########################
# Logging setup
# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Create a console handler and set the level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Add the formatter to the handler
ch.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(ch)
# Done with logging setup
#########################

def process_zip_file(myblob, dest_container_client):
    logger.debug("Starting process_zip_file")
    # Read the contents of the zip file
    data = myblob.read()
    #zip_file = zipfile.ZipFile(BytesIO(myblob))
    zip_file = zipfile.ZipFile(BytesIO(data))
    connect_str = os.getenv('A1_AZURE_STORAGE_CONNECTION_STRING')
    queue_name = os.getenv('A1_QUEUE_NAME')

    #zip_file = zipfile.ZipFile(myblob)
    for file in zip_file.namelist():
        #if file.endswith('.txt'):
            # Write each file in the zip file as a new blob in the destination container
        with zip_file.open(file) as txt_file:
            #contents = txt_file.read()
            # only get the file name - ignore the path from inside the zip file
            blob_client = dest_container_client.get_blob_client(os.path.basename(txt_file.name))
            blob_client.upload_blob(txt_file.read(), overwrite=True)
            queue_client = QueueClient.from_connection_string(conn_str=connect_str, queue_name=queue_name)
            queue_client.send_message(os.path.basename(txt_file.name))
