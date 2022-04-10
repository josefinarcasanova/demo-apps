#!/bin/sh
# -t = image tag

DOCKERHUB_NAME=""
while getopts t: option
	do
		case "${option}"
		in
			t) IMAGE_TAG=${OPTARG};;
		esac
done

[ -z "$IMAGE_TAG" ] && echo "Missing required -t flag for image tag"  && exit 1

docker build . -t ${IMAGE_TAG}

source .env

docker run -p $PORT:$PORT ${IMAGE_TAG}