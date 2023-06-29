This is an example of using managed identity to access blobs and queues. This project monitors an Azure blob storage container for new zip files. The code reads the zip contents and drops each file into the destination blob container. Each filename is pushed onto a queue.

To do: verify the test user has access to read/write the queue