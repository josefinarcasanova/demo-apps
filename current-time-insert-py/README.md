# Current Time Insert PY

A mock-up Python application that inserts a JSON on a MongoDB database containing the current day and time.

- [Current Time Insert PY](#current-time-insert-py)
  - [File Structure](#file-structure)
  - [Environment variables](#environment-variables)
  - [Run app locally](#run-app-locally)
    - [Using Python](#using-python)
    - [Using Docker](#using-docker)

- - - 

## File Structure

This app has a few important files:

- a `Dockerfile`, which will build the container image based on the source code
- Application dependencies on the `requirements.txt` file
- A `src` folder containing the app's source code. There you'll find:
  - `database.py` file containing scripts for altering and interacting with the MongoDB database
  - `icos.py` script regarding connection and file downloads from IBM Cloud Object Storage (ICOS)
  - `main.js`, which is the main program
  - `.env` file containing all the environment variables

## Environment variables

The app uses the following environment variables:

- `MONGO_URL`: mongodb URI connection string. See more info [in the docs](https://www.mongodb.com/docs/manual/reference/connection-string/)
- `replicaSet`: mongodb's replica set value. Default: `replset`
- `TLS_FILE_NAME`: name of the database TLS certificate file. Same value as the key identifying such file on ICOS
- `MONGO_DB_NAME`: database name. Default: `admin`
- `MONGO_COLLECTION_NAME`: collection where data will be inserted/retrieved
- `COS_API_KEY_ID`: ICOS instance's APIKEY value. Can be obtained from the instance's `Service Credentials` section on IBM Cloud.
- `COS_INSTANCE_ID`: : ICOS instance ID. Can be obtained from the instance's `Service Credentials` section on IBM Cloud.
- `COS_ENDPOINT`. ICOS endpoint. **Not** to be confused with the value found on `Service Credentials`. For more info, see [Endpoints and storage locations](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints) Default: `https://s3.us-south.cloud-object-storage.appdomain.cloud`
- `COS_BUCKET_NAME`: bucket name where the info will be retrieved/stored
- `COS_BUCKET_LOCATION`. Bucket location/region. Default: `us-south`

- - -

## Run app locally

CD to the repository directory:

```bash
cd /repository/directory
```

- - - 

### Using Python

Install dependencies by running:

```
pip install -r requirements.txt
```

Run app by running:

```
cd ./src
python main.py
```

### Using Docker

Build the image:

```bash
docker build . -t <image_tag>
```

**Note:** for uploading to IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

- - - 

Run it:

```bash
docker run <image_tag>
```

- - - 

If you can't remember the image tag, list them by running:

```bash
docker image list
```