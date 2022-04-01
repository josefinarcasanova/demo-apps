# Hello World JS

A pretty simple "Hello World" application written using Node.js. Nothing fancy, just functional.

This sample has a few important files:

- an `.env` file containing all the environment variables
- a `Dockerfile`, which will build the container image based on the source code
- Node dependencies on the `package-lock` and `package` JSON files.
- `server.js` the fancy little program
- a `build-and-run.sh` shell script to automate the process of building and running the app using Docker

It also has a `tekton` folder where you'll find `YAML` files to create deployments and pipelines for this application, to be used in a Kubernetes environment.

## Run app manually on a local environment

CD to the repository directory:

```bash
cd /repository/directory
```

- - - 

Build the image:

```bash
docker build . -t <image_tag>
```

**Note:** for uploading to IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

- - - 

Run it:

```bash
docker run -p <PORT>:<PORT> <image_tag>
```

**Note:** by default, the application uses port 8080, but another could be used. Check the [.env file](.env)to make sure you're using the correct value.

- - - 

If you can't remember the image tag, list them by running:

```bash
docker image list
```

## Run app through the shell script

CD to the repository directory:

```bash
cd /repository/directory
```

Run the shell script:

```
sh build-and-run.sh -t <image_tag>
```

This will build the image tagging it with the `<image_tag>` value you sent as argument, load environment variables from the `.env` file, and run it, exposing the port defined there.