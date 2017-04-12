FROM ubuntu:latest
MAINTAINER Savithru Lokanath "savithru@icloud.com"
RUN apt-get update -y
RUN apt-get install -y python-pip vim curl net-tools
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE  80
ENTRYPOINT ["python"]
CMD ["app.py"]
