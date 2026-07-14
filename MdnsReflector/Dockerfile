FROM alpine

ENV LANG=C.UTF-8

COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf
COPY run.sh /run.sh

RUN apk add --no-cache avahi avahi-tools tcpdump netcat-openbsd bash && chmod +x /run.sh
RUN rm -rf /etc/avahi/services/*

ENTRYPOINT ["/run.sh"]
