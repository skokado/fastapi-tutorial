My Tutorial app from [Full Course Youtube](https://www.youtube.com/watch?v=7t2alSnE2-I&t=13684s)

https://github.com/bitfumes/fastapi-course

# Developement

```shell
$ pipenv sync --dev
$ pipenv shell
```

## DBコンテナ起動

`.env`を編集

```shell
PGUSER=app
PGPASSWORD=***
PGHOST=127.0.0.1
PGPORT=5432
PGDATABASE=app

ADMIN_SECRET_KEY=***
```

```shell
$ # Postgresql
$ docker run -d --rm \
   --name db \
  -p 5432:5432 \
  -e POSTGRES_USER=app \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=app \
  postgres:13.4

$ # redis
$ docker run -d --rm \
   --name redis \
  -p 6379:6379 \
  redis:6.2.5
```

## マイグレーション

```shell
$ alembic upgrade head
```
