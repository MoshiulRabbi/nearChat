FROM python:3.9.6-alpine
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 8000

COPY . /app

WORKDIR /app