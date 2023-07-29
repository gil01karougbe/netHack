FROM ubuntu:latest

# Update package lists and install necessary tools
RUN apt-get update && apt-get install -y \
    macchanger \
    net-tools \
    iproute2 \
    network-manager \
    iputils-ping \
    arp-scan

COPY ./notes.txt /notes.txt
# Set the entry point as bash
CMD ["/bin/bash"]
