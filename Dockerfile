FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./app /usr/src/app

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile /usr/src
COPY Pipfile.lock /usr/src

WORKDIR /usr/src
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy