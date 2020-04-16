FROM python:2.7-slim

LABEL maintainer="https://github.com/alibo"

ARG BOMBSQUAD_VERSION="1.4.153"


RUN apt-get -y update && apt-get install -y locales libsdl2-2.0-0 wget && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

WORKDIR /app

RUN wget https://files.ballistica.net/bombsquad/builds/BombSquad_Server_Linux_64bit_${BOMBSQUAD_VERSION}.tar.gz -O bombsquad.tar.gz && \
    tar xzvf bombsquad.tar.gz && \
    mv BombSquad_Server*/ bombsquad-server && \
    rm -f bombsquad.tar.gz

WORKDIR /app/bombsquad-server

EXPOSE 43210/udp

CMD ["/app/bombsquad-server/bombsquad_server"]
