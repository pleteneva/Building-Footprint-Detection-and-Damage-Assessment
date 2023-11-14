#!/bin/bash
set -o errexit
export DOCKER_BUILDKIT=1
export PROGRESS_NO_TRUNC=1

# shellcheck disable=SC2046
docker build --tag kp_ubuntu_image \
    --build-arg USER_ID=$(id -u) \
    --build-arg GROUP_ID=$(id -g) \
    --build-arg WORKDIR_PATH=$(pwd) .

# shellcheck disable=SC2046
docker run \
    --name=asg_lt \
    --shm-size 2G \
    --rm \
    -u $(id -u):$(id -g) \
    -v $(pwd):$(pwd):rw \
    --gpus '"device=0"' \
    --cpuset-cpus "0-10" \
    -it \
    --entrypoint /bin/bash \
    kp_ubuntu_image:latest

docker image rm kp_ubuntu_image
