FROM kalilinux/kali-rolling:latest

RUN \
  apt-get update && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install iputils-ping && \
  apt-get install net-tools && \
  apt-get install -y python3 python3-pip && \
  pip3 install scapy && \
  apt-get install -y nano && \
  apt-get install -y tcpdump && \
  apt-get install -y procps  && \
  apt-get install -y arp-scan


COPY ./arp_poison.py  /arp_poison.py
COPY ./notes.txt      /notes.txt
COPY ./tcpjack.py     /tcpjack.py

CMD ["bash"]
