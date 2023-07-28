# MusicShop

## About Project

An e-commerce project using Django Framework and Django REST Framework to sell various musical instruments.

Link to the project website: http://djangomusicshop.ru/

## Features
- **[Python](https://www.python.org/)** (version 3.8)
- **[Django](https://www.djangoproject.com/)**
- **[DRF](https://www.django-rest-framework.org/)**
- **[PostgreSQL](https://www.postgresql.org/)**
- **[Docker Compose](https://docs.docker.com/compose/)**
- **[Redis](https://redis.io/)**

## Quickstart

First, clone project

``` 
git clone https://github.com/Niolum/MusicShop.git
```

Then, create .env file. set environment variables and create database.

Example ``.env``:

```
DEBUG=0
SECRET_KEY="some_secret_key"
ALLOWED_HOSTS="*"

CACHEOPS_REDIS=redis://localhost:6379/0

DBUSER=username
DBPASS=password
DBNAME=db_name
DBHOST=localhost
DBPORT=5432
```

Further, set up the virtual environment and the main dependencies from the ``requirements.txt``

```
python -m venv venv
source venv/bin/activate 
# or for windows
venv/Scripts/activate 
pip install -r requirements.txt
```

Before starting, you need to execute several commands:

```
python manage.py migrate
python manage.py loaddata user/fixtures/user.json cart/fixtures/cart.json product/fixtures/product.json
python manage.py collectstatic
```

Run application:

```
python manage.py runserver
```

For start in docker-compose change .env:

```
DEBUG=0
SECRET_KEY="django-insecure-fqqw64n@$qxu&g0sv0w07-^$q22l%5rusi+h-tils+xv1+e$"
ALLOWED_HOSTS="*"

CACHEOPS_REDIS=redis://redis_cache:6371/1

POSTGRES_USER=username
POSTGRES_PASSWORD=some_password
POSTGRES_DB=some_name_db

DBUSER=username
DBPASS=some_password
DBNAME=some_name_db
DBHOST=shopdb
DBPORT=5431
```

Before running docker-compose:

```
docker volume create static_django_shop
docker volume create media_django_shop
docker volume create django_musicshop_db
docker network create —driver bridge —subnet 172.26.0.0/24 testnet
```

To start the project, use the following command:

```
docker-compose up -d
```