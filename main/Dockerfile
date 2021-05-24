# Image of python in version 3.8
FROM python:3.8

# Environment variable useful to get logs
ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app