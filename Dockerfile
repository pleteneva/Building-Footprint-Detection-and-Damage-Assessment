FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
ENV TERM=linux DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8 LC_ALL C.UTF-8  PYTHONDONTWRITEBYTECODE=1
RUN apt-get update -qq -o=Dpkg::Use-Pty=0 && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-ipdb \
        python3-pip \
        ipython3 \
        python3-opencv \
        vim && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install \
        'numpy==1.22.4' \
        'building_footprint_segmentation==0.2.4' \
        'image-fragment==0.2.3' \
        'shapely==1.8.0' \
        'skimage==1.10.0' \
        'torch==2.1.0' \
        'torchvision==0.14.1' \
        'opencv-python-headless==4.7.0.72'
RUN sed -i "/PS1=/s/PS1=.*/PS1='\\\h:\\\w\\\\$ '/" /etc/bash.bashrc
WORKDIR /w
