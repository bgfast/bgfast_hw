# BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `samples/{name}.png` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

# prereqs:
# Install the Azure Storage Queue library
python -m venv .venv
pip install azure-functions
pip install azure-storage-queue
pip install azure-storage-blob azure-identity
pip freeze > requirements.txt
# if you are using Python 2.x, you should use pip. If you are using Python 3.x, you should use pip3
pip install -r requirements.txt

# Python 3.10.x
# error with system.net.http.formatting
# https://stackoverflow.com/questions/73034959/microsoft-azure-webjobs-extensions-http-could-not-load-file-or-assembly
# Install-Package Microsoft.AspNet.WebApi.Client 
<TODO> Documentation