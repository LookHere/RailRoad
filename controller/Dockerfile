FROM balenalib/raspberrypi3-ubuntu-python:3.8-bionic-build

WORKDIR /usr/src/app

#RUN apt-get update && apt-get install -y ttf-dejavu libfreetype6-dev

RUN pip3 install RPi.GPIO

COPY *.py ./
COPY *.mp3 ./
COPY *.wav ./

CMD [ "sleep", "infinity" ]
