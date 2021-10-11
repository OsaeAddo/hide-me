FROM python:3.8-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /hide-me

COPY Pipfile Pipfile.lock /hide-me/
RUN pip install pipenv && pipenv install --system

COPY . /hide-me/