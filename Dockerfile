FROM python:3.9.16-alpine3.16
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN adduser --disabled-password service-user 
RUN apk add postgresql-client build-base postgresql-dev

WORKDIR /todo
COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
COPY todo /todo
EXPOSE 8000
