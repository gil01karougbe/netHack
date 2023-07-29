FROM ubuntu:latest

RUN apt-get update

RUN \
  apt-get install -y net-tools && \
  apt-get install -y iputils-ping && \
  apt-get install -y nano && \
  apt-get install -y iproute2 && \ 
  apt-get install -y telnet && \
  apt-get install -y telnetd

# Set password for the 'root' user
RUN echo 'root:root' | chpasswd

EXPOSE 23

RUN service openbsd-inetd start

COPY ./start.sh /start.sh
