FROM alpine:3.2

ENV TCPDUMP_VERSION 4.7.4-r0

RUN apk add --update
RUN apk add tcpdump
VOLUME ["/data"]
ENTRYPOINT ["/usr/sbin/tcpdump"]
