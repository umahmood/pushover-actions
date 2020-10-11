FROM python:3.8.6-slim-buster

LABEL "version"="1.0.0"

WORKDIR /home

COPY . .

RUN pip install requests

ENTRYPOINT ["python3", "/home/pushover.py"]
