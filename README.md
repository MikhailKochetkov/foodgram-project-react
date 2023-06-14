## Описание проекта
Проект «Продуктовый помощник» - это приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд по рецепту.

### Запуск проекта в Docker на localhost

В директории infra создать файл .env:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Собрать контейнеры:

```bash
docker-compose up -d --build
```

Остановить контейнеры: 

```bash
docker-compose stop
```

Выполнить миграции:

```bash
docker-compose exec web python manage.py makemigrations
```

```bash
docker-compose exec web python manage.py migrate --noinput
```

Создать суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```bash
docker-compose exec web python manage.py collectstatic --no-input
```

### Документация к API доступна по ссылке

```url
http://127.0.0.1/api/docs/redoc.html
```
