ARG BUILD_FROM
FROM $BUILD_FROM

MAINTAINER micmoc95 <mic.morat@gmail.com>

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
