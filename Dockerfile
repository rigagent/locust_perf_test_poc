FROM python:3.9

USER root
WORKDIR /load
ENV PYTHONPATH=/load
COPY . .
RUN pip3 install -r /load/requirements.txt
