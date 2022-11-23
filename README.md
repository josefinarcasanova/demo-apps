# Demo Apps

This repository is meant to store small demo applications for showcasing IBM Cloud services like Code Engine, Red Hat OpenShift, Kubernetes Service, among others.

I've decided to leave this repo public in case someone else wants to try them out.

- [Demo Apps](#demo-apps)
  - [Catalog](#catalog)
  - [Running containerized apps locally](#running-containerized-apps-locally)
  - [Pushing container images to ICR](#pushing-container-images-to-icr)

## Catalog

Demos apps available are:

<!--
- [current-time-insert-py](./current-time-insert-py/)
  - **Description:** application that inserts a JSON on a MongoDB database containing the current day and time. Pulls data from Cloud Object Storage for database authentication.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of application integration, or batch processes (Code Engine Jobs).
- [current-time-print-py](./current-time-insert-py/)
  - **Description:** application that prints the current day and time.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Batch processes (Code Engine Jobs).
- [hello-world-js](./hello-world-js/)
  - **Description:** exposes a server (on port 8080 by default) with a "Hello ${TARGET}" message.
  - **Use Cases:** application deployment on any PaaS service (RHOS, IKS, CE). **Update:** can also be used to show how environment variables work, since I've added them for both `TARGET` and `PORT`.
- [send-email-app](./send-email-app)
  - **Description:** application that sends emails via SendGrid. **Note:** it is untested due to invalid SendGrid credentials.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of on-demand code executions.
-->

App                                                       | Description                                                                     | Use Cases
----------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------
[current-time-insert-py](./current-time-insert-py/)       | Inserts a JSON on a MongoDB database containing the current day and time. Pulls data from ICOS for database authentication. | FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of application integration, or batch processes (Code Engine Jobs).
[current-time-print-py](./current-time-insert-py/)        | Prints current day and time.                                                    | FaaS-related use cases. Batch processes (Code Engine Jobs).
[hello-world-js](./hello-world-js/)                       | Exposes a server with a `Hello ${TARGET}` message. Uses environment variables. Provides YAML manifests for IKS/ROKS deployments. | Environment variables. App deployment on PaaS services (RHOS, IKS, CE).

## Running containerized apps locally

Change directory to where the repository is:

```bash
cd /<repository-directory>
```

Build the image:

```bash
docker build . --tag <image_tag>
```

> **Note:** for using IBM Container registry, `<image_tag>` format should be `<region>.icr.io/<my_namespace>/<my_repository>:<my_tag>`

Run application.

```bash
docker run -p <local-port>:<container-port> <image_tag>
```

Where:

- `<local-port>`: host machine (`127.0.0.1`) port.
- `<container-port>`: container port. It's the one you expose on your Dockerfile, or through environment variables.
- `<image_tag>`: image tag.

For more info see the [command reference](https://docs.docker.com/engine/reference/commandline/run/).

> **Note:** if you can't remember the image tag, list them by running `docker image list`.

## Pushing container images to ICR

Push image to IBM Container Registry (ICR) by running:

```bash
docker push <image_tag>
```

Where `<image_tag>` has the following format: `<region>.icr.io/<namespace>/<repository>:<tag>`. For more info about regions, [check out the docs](https://cloud.ibm.com/docs/Registry?topic=Registry-registry_overview#registry_regions).

- - - 

If the image isn't tagged this way, fix it by re-tagging it. Just run:

```bash
docker tag <current_tag> us.icr.io/<namespace>/<repository>:<tag>
```