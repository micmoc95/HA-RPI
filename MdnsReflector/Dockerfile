FROM alpine

ENV LANG=C.UTF-8

COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf
COPY run.sh /run.sh

RUN apk add --no-cache avahi tcpdump bash && chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
