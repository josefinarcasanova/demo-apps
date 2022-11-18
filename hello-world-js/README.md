# Hello World JS

A pretty simple "Hello World" application written using Node.js. Nothing fancy, just functional.

- [Hello World JS](#hello-world-js)
  - [File Structure](#file-structure)
  - [Environment variables](#environment-variables)
  - [Runing the app](#runing-the-app)
    - [Using Docker](#using-docker)
    - [Using a Shell Script](#using-a-shell-script)
  - [Deploying to IBM Kubernetes Service](#deploying-to-ibm-kubernetes-service)
    - [References](#references)

- - - 

## File Structure

This sample has a few important files:

- an `.env` file containing all the environment variables
- a `Dockerfile`, which will build the container image based on the source code
- Node dependencies on the `package-lock` and `package` JSON files.
- `server.js` the fancy little program
- a `build-and-run.sh` shell script to automate the process of building and running the app using Docker

It also has a `tekton` folder where you'll find `YAML` files to create deployments and pipelines for this application, to be used in a Kubernetes environment.

## Environment variables

The app uses the following environment variables:

- `TARGET`: target the app will say hello to. Default: `World`.
- `PORT`: port the app will run on. Default: `8080`.

- - -

## Runing the app 

### Using Docker

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

**Note:** by default, the application uses port 8080, but another could be used. Check the [.env file](.env) to make sure you're using the correct value.

- - - 

If you can't remember the image tag, list them by running:

```bash
docker image list
```

### Using a Shell Script

CD to the repository directory:

```bash
cd /repository/directory
```

Run the shell script:

```
sh build-and-run.sh -t <image_tag>
```

This will build the image tagging it with the `<image_tag>` value you sent as argument, load environment variables from the [.env file](.env), and run it, exposing the port defined there.

## Deploying to IBM Kubernetes Service

To create a secret to pull images from IBM Container Registry, you must first create a [Service ID](https://cloud.ibm.com/iam/serviceids), assign policies to enable access to IBM Container Registry, and [create an API Key](https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui#create_user_key) associated to it as means of authentication. See [Setting up an image registry](https://cloud.ibm.com/docs/containers?topic=containers-registry#other_registry_accounts) for more information.

Create an IBM Cloud IAM [service ID](https://cloud.ibm.com/docs/account?topic=account-serviceids&interface=ui):

```
ibmcloud iam service-id-create <sid-name> --description "<some-description>"
```

Then, create a custom IBM Cloud IAM policy for your cluster service ID that grants access to IBM Cloud Container Registry.

```
ibmcloud iam service-policy-create <cluster_service_ID> --roles <service_access_role> --service-name container-registry [--region <IAM_region>] [--resource-type namespace --resource <registry_namespace>]
```

Create an API Key on IBM Cloud:

```
ibmcloud iam service-api-key-create <cluster_name>-<namespace>-key <cluster_name>-<namespace>-id --description "API key for service ID <service_id> in Kubernetes cluster <cluster_name> namespace <namespace>"
```

Now, log into your cluster, and create the Secret:

```
kubectl --namespace <namespace> create secret docker-registry <secret-name> \
    --docker-server=https://<region>.icr.io \
    --docker-username=iamapikey \
    --docker-password=<api-key> \
    --docker-email=<docker-email>
```

And apply the deployment YAML found at the [`kubernetes` folder](./kubernetes/):

```
kubectl apply -f deployment.yaml
```

### References

- [Documentation - Setting up an image registry](https://cloud.ibm.com/docs/containers?topic=containers-registry#other_registry_accounts)