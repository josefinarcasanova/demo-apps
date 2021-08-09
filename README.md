# Hello

A pretty simple node.js application. Gotta start some place.

- - -

This sample has two pieces:

- a `build` script which will build the container image(s) used
- a `run` script which deploys resources that use those images

## Run locally

CD to the repository directory:

```bash
cd /repository/directory
```

Build the image:

```bash
docker build . <image_tag>
```

**Note:** for using IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

Run it:

```bash
docker run -p 8080:8080 <image_tag>
```

If you can't remember the image tag, run:

```bash
docker image list
```

To list all built images.