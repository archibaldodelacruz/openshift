FROM ubuntu:latest
MAINTAINER Savithru Lokanath "savithru@icloud.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install tornado flask-googlemaps
RUN pip3 install --upgrade requests
EXPOSE  9090
ENTRYPOINT ["python3"]
CMD ["serve.py","9090"]
