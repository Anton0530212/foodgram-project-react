# Foodgram - Продуктовый помощник

![example workflow](https://github.com/Anton0530212/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Стек технологий

Python 3,
Django 2.2,
Django REST Framework,
PostgreSQL,
Nginx,
Gunicorn,
Docker,
GitHub Actions,
Yandex.Cloud.

## Описание проекта

Foodgram - лучший сервис для публикации рецептов.  
Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и скачивать его в pdf формате.

## Установка проекта локально

* Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Anton0530212/foodgram-project-react.git
```

```bash
cd foodgram-project-react
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/scripts/activate
```

* Cоздать файл `.env` в директории `/infra/` с содержанием:

```
SECRET_KEY=секретный ключ django
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

* Перейти в директирию backend, обновить менеджер пакетов и установить зависимости из файла requirements.txt:

```bash
cd backend/
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

* Выполнить миграции:

```bash
python manage.py migrate
```

* Загрузить ингридиенты и теги:

```bash
python manage.py load_ingrs
```

```bash
python manage.py load_tags
```

* Собрать статику:

```bash
python manage.py collectstatic --noinput
```

* Запустите сервер:

```bash
python manage.py runserver
```

## Запуск проекта в Docker-контейнере

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf` которые находятся в директории `infra/`.  
При необходимости добавьте/измените адреса проекта в файле `nginx.conf`

* Запустить docker-compose:
```bash
docker-compose up -d --build
```  
  > После сборки появляются 3 контейнера:
  > 1. контейнер базы данных **db**
  > 2. контейнер приложения **backend**
  > 3. контейнер web-сервера **nginx**
* Применить миграции:
```bash
docker-compose exec backend python manage.py migrate
```
* Загрузить ингредиенты:
```bash
docker-compose exec backend python manage.py load_ingrs
```
* Загрузить теги:
```bash
docker-compose exec backend python manage.py load_tags
```
* Создать суперпользователя:
```bash
docker-compose exec backend python manage.py createsuperuser
```
* Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```
## Сайт
Сайт доступен по ссылке:
[http://158.160.34.14/](http://158.160.34.14/)

## Документация к API
API документация доступна по ссылке:
[http://158.160.34.14/api/docs/](http://158.160.34.14/api/docs/)

## Авторы
[Плотицын Антон](https://github.com/Anton0530212) - Разработал бэкенд и деплой сервиса.
[Яндекс.Практикум](https://github.com/yandex-praktikum) - Фронтенд для сервиса.
