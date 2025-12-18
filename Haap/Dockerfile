ARG BUILD_FROM
FROM $BUILD_FROM

MAINTAINER micmoc95 <mic.morat@gmail.com>

RUN apt-get update && \
    apt-get install -y network-manager dbus && \
    apt-get clean

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
