FROM python:3.5
MAINTAINER Jonas Hedman Engström <jonas.hedeng@gmail.com>
COPY requirements.txt /opt/www/
RUN pip install -r /opt/www/requirements.txt
COPY . /opt/www/
WORKDIR /opt/www
CMD ["python", "app.py"]
