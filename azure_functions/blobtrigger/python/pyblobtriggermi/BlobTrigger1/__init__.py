import azure.functions as func
from azure.storage.blob import BlobServiceClient
from io import BytesIO
import json
import logging
import os
import sys
import zipfile

import azure.functions as func

# Get the absolute path of the Common directory
common_dir = os.path.abspath (os.path.join (os.path.dirname (__file__), "..", "common"))

# Add the Common directory to the sys.path
sys.path.append (common_dir)

# Import the helpers module
import ziphelper


fv = "0.0.2"
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

#def process_zip_file(myblob, dest_container_client):
#    logger.debug("{fv} Starting process_zip_file")
#    # Read the contents of the zip file
#    data = myblob.read()
#    #zip_file = zipfile.ZipFile(BytesIO(myblob))
#    zip_file = zipfile.ZipFile(BytesIO(data))
#
#    #zip_file = zipfile.ZipFile(myblob)
#    for file in zip_file.namelist():
#        #if file.endswith('.txt'):
#            # Write each file in the zip file as a new blob in the destination container
#        with zip_file.open(file) as txt_file:
#            #contents = txt_file.read()
#            # only get the file name - ignore the path from inside the zip file
#            logger.debug("{fv} Saving {txt_file.name} to {dest_container_client}")
#            blob_client = dest_container_client.get_blob_client(os.path.basename(txt_file.name))
#            blob_client.upload_blob(txt_file.read(), overwrite=True)
#    logger.debug("{fv} Finished process_zip_file")


# This function takes in a blob, gets the destination container information and calls process_zip_file
def main(myblob: func.InputStream):
    logging.info(f"{fv} Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # read the environment variables from local.settings.json
    


    connect_str = os.getenv('A1_AZURE_STORAGE_CONNECTION_STRING')
    dest_container_name = os.getenv('A1_DEST_CONTAINER_NAME')

    # validate the environment variables
    if connect_str is None:
        logger.error("{fv} A1_AZURE_STORAGE_CONNECTION_STRING is None")
        return
    if dest_container_name is None:
        logger.error("{fv} A1_DEST_CONTAINER_NAME is None")
        return

    if myblob is None:
        logger.debug("{fv} myblob is None. getting func.InputStream()")
        myblob = func.InputStream()
    #logging.info(f"Python blob trigger function processed blob \n"
    #             f"Name: {myblob.name}\n"
    #             f"Blob Size: {myblob.length} bytes")
    # Get the connection string for the storage account.
    # Create a BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # Create a container client object
    dest_container_client = blob_service_client.get_container_client(dest_container_name)
    # Create a blob client object for the destination blob
    #blob_client = dest_container_client.get_blob_client(myblob.name)
    
    ziphelper.process_zip_file(myblob, dest_container_client)
