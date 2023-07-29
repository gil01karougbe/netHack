# Use the Python 3 base image
FROM python:3

# Install Scapy and any other dependencies
RUN pip install scapy

# Copy your application code to the container
COPY ./arp_poison.py  /arp_poison.py
COPY ./notes.txt      /notes.txt

RUN apt-get update && apt-get install -y \
    iputils-ping \
    iproute2 \
    net-tools \
    iputils-ping \
    arp-scan
