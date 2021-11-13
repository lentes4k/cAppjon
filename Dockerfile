FROM python:3.10-alpine

RUN adduser --home /home/anotador --shell /bin/bash -D anotador && mkdir /cappjon
RUN chown -R anotador:anotador /cappjon
RUN apk add build-base #instalar gcc
RUN apk add libffi-dev #necesario para poetry

USER anotador
WORKDIR /cappjon
COPY poetry.lock pyproject.toml /cappjon/

ENV PATH="$PATH:/home/anotador/.local/bin"

RUN  pip3 install poetry

ENTRYPOINT ["poetry", "run", "test"]


