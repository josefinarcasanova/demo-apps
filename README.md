# DEMO APPS

This repository is meant to store my containerized applications for demo deployments using PaaS IBM Cloud services like Code Engine and Kubernetes Service. 

Currently, we have the following apps:

- [connect-mongodb-py](./connect-mongodb-py)
  - **Description:** application that inserts a JSON on a MongoDB database containing the current day and time.)
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine. Examples of application integration, or batch processes (Code Engine Jobs).
- [hello-world-js](./hello-world-js/)
  - **Description:** exposes a server on port 8080 with a "Hello World" message
  - **Use Cases:** application deployment on any PaaS service (RHOS, IKS, CE)
- [send-email-app](./send-email-app)
  - **Description:** application that sends emails via SendGrid. *Note:* it is untested due to invalid SendGrid credentials.
  - **Use Cases:** FaaS-related use cases, be it on Cloud Functions or Code Engine.

## Run containerized apps locally

CD to the repository directory:

```bash
cd /repository/directory
```

- - - 

Build the image:

```bash
docker build . --tag <image_tag>
```

**Note:** for using IBM Container registry, `<image_tag>` format should be `us.icr.io/<my_namespace>/<my_repository>:<my_tag>`

- - - 

Run it:

```bash
docker run -p 8080:8080 <image_tag>
```

**Note:** another port could be used. Validate if project has an environment variable defined or it.

- - - 

If you can't remember the image tag, run:

```bash
docker image list
```

To list all built images.

## Push images to ICR

Push image to ICR

```bash
docker push <image_tag>
```

Where `<image_tag>` has the following format: `<region>.icr.io/<namespace>/<repository>:<tag>`

- - - 

If the image isn't tag in this way, fix it by re-tagging it:

```bash
docker tag <local_tag> us.icr.io/<namespace>/<repository>:<tag>
```