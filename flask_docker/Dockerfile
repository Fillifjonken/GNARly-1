FROM ubuntu:14.04
MAINTAINER Jonas Hedman Engström <jonas.hedeng@gmail.com>
RUN apt-get update && apt-get install -y python python-pip
COPY requirements.txt /opt/www/
RUN pip install -r /opt/www/requirements.txt
COPY . /opt/www/
WORKDIR /opt/www
CMD ["python", "app.py"]
