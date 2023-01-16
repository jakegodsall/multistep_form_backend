FROM python:3.11.1-alpine3.17

ENV PYTHONUNBUFFERED 1

WORKDIR /multistep_form_backend

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["adduser", "-D", "user"]

USER user
