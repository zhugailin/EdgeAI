FROM ubuntu:18.04 

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git curl gnupg

# Install PyCoral
env http_proxy "socks5://192.168.57.198:10808"
env https_proxy "socks5://192.168.57.198:10808"
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

ENV http_proxy " "
ENV https_proxy " "
RUN apt-get update && apt-get install -y gasket-dkms libedgetpu1-std python3-pycoral


RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip setuptools wheel
RUN python3 -m pip install numpy
RUN python3 -m pip install opencv-python-headless
RUN python3 -m pip install tqdm pyyaml json

# Mountpoint for yolo testing
RUN mkdir /yolo
