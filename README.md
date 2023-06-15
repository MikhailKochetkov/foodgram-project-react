## Описание проекта
Проект «Продуктовый помощник» - это приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд по рецепту.

## Запуск проекта на удаленном сервере:

Клонировать репозиторий:
```bash
git clone git@github.com:MikhailKochetkov/foodgram-project-react.git
```

Установить на сервере Docker, Docker Compose:
```bash
sudo apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
sudo apt-get install docker-compose-plugin
```

Скопировать на сервер файлы docker-compose.yml, default.conf из папки infra
```bash
scp docker-compose.yml nginx.conf username@IP:/home/username/
scp nginx.conf username@IP:/home/username/nginx
```

Создать переменные окружения для работы с GitHub Actions
```bash
DOCKER_PASSWORD         - пароль Docker Hub
DOCKER_USERNAME         - логин Docker Hub
HOST                    - публичный IP сервера
USER                    - имя пользователя на сервере
PASSPHRASE              - *создается, если ssh-ключ защищен паролем
SSH_KEY                 - приватный ssh-ключ
TELEGRAM_TO             - ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          - токен телеграм-бота, посылающего сообщение
DB_ENGINE               - django.db.backends.postgresql
DB_NAME                 - postgres
POSTGRES_USER           - postgres
POSTGRES_PASSWORD       - postgres
DB_HOST                 - db
DB_PORT                 - 5432
```

Создать и запустить контейнеры Docker:
```bash
sudo docker compose up -d
```

Выполнить миграции:
```bash
sudo docker compose exec backend python manage.py migrate
```

Собрать статику:
```bash
sudo docker compose exec web python manage.py collectstatic --noinput
```

Создать суперпользователя:
```bash
sudo docker compose exec backend python manage.py createsuperuser
```

Остановить контейнеры:
```bash
sudo docker compose down -v      - остановка и удаление контейнеров
sudo docker compose stop         - остановка контейнеров без удаления
```

### Документация к API доступна по ссылке

```url
http://158.160.38.121/api/docs/redoc.html
```

## Запуск проекта на localhost

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
