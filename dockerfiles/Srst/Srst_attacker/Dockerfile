FROM kalilinux/kali-rolling:latest

RUN \
  apt-get update && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install iputils-ping && \
  apt-get install net-tools && \
  apt-get install -y nano && \
  apt-get install -y arp-scan && \
  apt-get install -y netwox && \
  apt-get install -y hping3


COPY ./notes.txt      /notes.txt

