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
        'numpy==1.23.5' \
        'building_footprint_segmentation==0.2.4' \
        'image-fragment==0.2.3' \
        'shapely==2.0.2' \
        'scikit-image==0.19.3' \
        'PyYAML==6.0.1' \
        'torch==2.1.0' \
        'torchvision==0.16.0' \
        'opencv-python-headless==4.8.1.78'
RUN sed -i "/PS1=/s/PS1=.*/PS1='\\\h:\\\w\\\\$ '/" /etc/bash.bashrc
WORKDIR /w
