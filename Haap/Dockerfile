ARG BUILD_FROM
FROM $BUILD_FROM

MAINTAINER micmoc95 <mic.morat@gmail.com>

RUN apk add --no-cache networkmanager networkmanager-cli dbus

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
