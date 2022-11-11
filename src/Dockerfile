FROM ubuntu

MAINTAINER PEMIDI <rashidi.peyman@gmail.com>

RUN mkdir /remindpo
WORKDIR /remindpo

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

RUN apt update
RUN apt install -y python3-pip

ADD requirements.txt /remindpo
RUN pip install -r requirements.txt
ADD . /remindpo




