FROM ubuntu:latest

RUN apt-get update

RUN \
  apt-get install -y net-tools && \
  apt-get install -y iputils-ping && \
  apt-get install -y nano && \
  apt-get install -y iproute2 && \ 
  apt-get install -y telnet

CMD ["bash"]
