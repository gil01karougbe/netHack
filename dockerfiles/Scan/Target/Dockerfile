FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y apache2 inetutils-telnetd vsftpd openssh-server

# Enable SSH
RUN mkdir /var/run/sshd && \
    echo 'root:root' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

# Configure FTP
RUN sed -i 's/#write_enable=YES/write_enable=YES/' /etc/vsftpd.conf && \
    sed -i 's/#chroot_local_user=YES/chroot_local_user=YES/' /etc/vsftpd.conf



COPY ./start.sh /start.sh
COPY ./notes.txt /notes.txt
# Expose ports
EXPOSE 80 23 21 22

# Start services
CMD service apache2 start && \
    service vsftpd start && \
    /usr/sbin/sshd -D
