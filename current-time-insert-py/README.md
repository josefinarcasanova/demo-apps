# Current Time PY

A mock-up Python application that inserts a JSON on a MongoDB database containing the current day and time.

- [Current Time PY](#current-time-py)
  - [File Structure](#file-structure)
  - [Run app locally](#run-app-locally)
    - [Using Python](#using-python)
    - [Using Docker](#using-docker)

- - - 

## File Structure

This app has a few important files:

- an `.env` file containing all the environment variables
- a `Dockerfile`, which will build the container image based on the source code
- Application dependencies on the `requirements.txt` file
- `database.py` which contains the scripts for altering and interacting with the MongoDB database
- And `main.js`, which is the main program

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