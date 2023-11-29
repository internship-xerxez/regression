FROM python:3.8-slim

LABEL maintainer="xerxez.in"

ENV PYTHONNUNBUFFERED 1

COPY ./requirements_docker.txt /requiremnets_docker.txt
COPY ./webapp /webapp
COPY ./models/model.joblib /models/model.joblib
COPY ./models/trained.h5 /models/trained.h5

WORKDIR /webapp

EXPOSE 8080

RUN python -m venv /py
#RUN /py/bin/pip install awscli -y
RUN /py/bin/pip install -r /requiremnets_docker.txt
RUN apt update -y && apt install awscli -y
RUN /py/bin/pip install --upgrade pip
RUN python -m pip install --upgrade pip


#RUN apk add --update --no-cache --virtual linux-headers
#RUN adduser --disable-password --no-create-home webapp

ENV PATH="/py/bin:$PATH"

#USER app

#USER webapp




