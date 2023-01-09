FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y

RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]










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
