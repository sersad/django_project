#### Описание

Это учебный проект Django. 

В директории `pg` находятся volume `postgres` и `pgadmin` для docker

В директории `static` находятся статические файлы bootstrap, css, img и т.п.

В директории `temlates` web шаблоны проекта.

В директории `fixtures` данные в формате yaml для первоначальной загрузки тестовых данных в проект.
Загрузка осуществляется 
`docker-compose run web python manage.py loaddata data`
Но работает только в том случае если новостей еще нет, так как новости прописаны без pk и есть ограничения на уникальность данных в таблице.

#### Запуск
Перед запуском проекта соберите контейнеры в корне

`docker-compose up -d --build`
#### URLs
- django http://127.0.0.1:8000
- админка django http://127.0.0.1:8000/admin/
- pgadmin http://127.0.0.1:5050/browser/

#### Используемые технологии

- [x] Django ORM база данных со множеством связей (например если удалить пользователя, то все его комментарии удалятся автоматически без доп запросов, тоже и с новостями)
- [x] Django Class-based views and dynamic filtering
- [x] Django templates
- [x] CSS + JS
- [x] Bootstrap
- [x] ААА средствами Django
- [x] Регистрация пользователя
- [ ] Восстановление пароля
- [x] Управление пользователями проекта Django из кастомной админ панели 
- [x] Разделение прав доступа по группам
- [ ] API
- [ ] Тесты
- [ ] Логирование
- [x] Docker и docker compose

#### Учетные данные
- root:123 админка django может только комментировать
- editor:123 может редактировать и добавлять новости
- reader:123 может только комментировать

#### Запуск команды migrate в контейнере

`docker-compose run web python manage.py migrate`

#### Создание супер пользователя root

`docker-compose run web python manage.py createsuperuser`
пароль `123`

#### добавление нового приложения

`docker-compose run web python manage.py startapp news`

#### загружаем фикстуры

`docker-compose run web python manage.py loaddata fixtures/data`

#### очистка всего старого в докере

`docker system prune -a -f`

#### что может понадобиться
https://www.twilio.com/blog/passwordless-authentication-system-django-twilio-verify-sendgrid?utm_campaign=Django%2BNewsletter&utm_medium=web&utm_source=Django_Newsletter_137

Руководство Django Часть 8: Аутентификация и авторизация пользователя - Изучение веб-разработки
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Authentication

Dockerizing Django with Postgres, Gunicorn, and Traefik
https://testdriven.io/blog/django-docker-traefik/

Изучаем Docker, часть 3: файлы Dockerfile
https://habr.com/ru/company/ruvds/blog/439980/

The login_required decorator login_required(redirect_field_name='next', login_url=None)[source]
https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.decorators.login_required%23django.contrib.auth.decorators.login_required


https://ordinarycoders.com/blog/article/django-user-register-login-logout
https://ordinarycoders.com/blog/article/django-password-reset


login.html lost password not work
