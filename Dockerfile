FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /musicshop
COPY requirements.txt /musicshop/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /musicshop/
EXPOSE 7000