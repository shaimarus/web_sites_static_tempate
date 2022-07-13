FROM python:3.9
RUN apt-get update 
RUN mkdir /opt/web/
COPY . /opt/web/

RUN pip3 install -r /opt/web/requirements.txt

WORKDIR /opt/web/

