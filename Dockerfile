FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /musicshop
COPY requirements.txt /musicshop/
COPY . /musicshop/
RUN pip install -r requirements.txt
EXPOSE 7000