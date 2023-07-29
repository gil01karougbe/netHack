FROM kalilinux/kali-rolling:latest

# Update package lists and install Nmap
RUN apt-get update && \
    apt-get install -y nmap

COPY ./notes.txt /notes.txt
