FROM python:3.10-alpine

RUN adduser --home /home/anotador --shell /bin/bash -D anotador && apk add build-base libffi-dev  #instalar gcc y libreria para poetry

USER anotador
WORKDIR /app/test/

ENV PATH="$PATH:/home/anotador/.local/bin"

RUN  pip3 install poetry

ENTRYPOINT ["poetry", "run", "test"]

