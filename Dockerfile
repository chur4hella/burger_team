FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1


RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

COPY . .










#FROM python:3.10
#
#ENV PIP_DISABLE_PIP_VERSION_CHECK 1
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#WORKDIR /code
#
#COPY ./req.txt .
#RUN pip install -r req.txt
#
#COPY . .
