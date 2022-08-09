#### Описание

Это учебный проект Django. 

В директории `pg` находятся volume `postgres` и `pgadmin` для docker

В директории `static` находятся статические файлы bootstrap, css, img и т.п.

В директории `temlates` web шаблоны проекта.

В директории `fixtures` данные в формате yaml для первоначальной загрузки тестовых данных в проект.
Загрузка первоночальных данных осуществляется 
`docker-compose run web python manage.py loaddata data`
Но работает только в том случае если новостей еще нет, так как новости прописаны без pk и есть ограничения на уникальность данных в таблице.

#### Запуск
Перед запуском проекта соберите контейнеры в корне командой

`docker-compose up -d --build`

#### URLs
- http://127.0.0.1:8000 - django
- http://127.0.0.1:8000/admin/ - админка django
- http://127.0.0.1:5050/browser/ - pgadmin

#### Используемые технологии

- [x] Django ORM база данных со множеством связей (например если удалить пользователя, то все его комментарии удалятся автоматически без доп запросов, тоже и с новостями)
- [x] Django Class-based views and dynamic filtering
- [x] Django templates
- [x] CSS + JS
- [x] Bootstrap
- [x] WYSIWYG редактор для новостей
- [x] ААА средствами Django
- [x] Регистрация пользователя
- [ ] Восстановление пароля (необходим почтовый сервак можно его в докере поднять, но не входит в задачу проекта)
- [x] Управление пользователями проекта Django из кастомной админ панели 
- [x] Разделение прав доступа по группам
- [x] API
- [ ] Тесты
- [ ] Логирование
- [x] Docker и docker compose

#### Учетные данные
- root:123 админка django может только комментировать
- editor:123 может редактировать и добавлять новости
- reader:123 может только комментировать

#### API URLs
- http://127.0.0.1:8000/api/users/ - пользователи
- http://127.0.0.1:8000/api/groups/ - группы
- http://127.0.0.1:8000/api/news/ - новости
- http://127.0.0.1:8000/api/category/ - категории новостей
- http://127.0.0.1:8000/api/comments/ - комментарии

#### TODO
Для формы регистрации и авторизации messages не работают

https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
https://django.fun/docs/django/ru/4.0/ref/contrib/messages/

Восстановление пароля

https://ordinarycoders.com/blog/article/django-password-reset
https://ordinarycoders.com/blog/article/django-user-register-login-logout

Логирование
https://docs.djangoproject.com/en/4.1/topics/logging/

Перевод веба на Traefik в контейнере
https://testdriven.io/blog/django-docker-traefik/

#### Загрузка фикстур

`docker-compose run web python manage.py loaddata fixtures/data`

#### Очистка всего старого в докере

`docker system prune -a -f`


#### Разное и полезное
https://www.twilio.com/blog/passwordless-authentication-system-django-twilio-verify-sendgrid?utm_campaign=Django%2BNewsletter&utm_medium=web&utm_source=Django_Newsletter_137

Руководство Django Часть 8: Аутентификация и авторизация пользователя - Изучение веб-разработки
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Authentication

Dockerizing Django with Postgres, Gunicorn, and Traefik
https://testdriven.io/blog/django-docker-traefik/

Изучаем Docker, часть 3: файлы Dockerfile
https://habr.com/ru/company/ruvds/blog/439980/

The login_required decorator login_required(redirect_field_name='next', login_url=None)[source]
https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.decorators.login_required%23django.contrib.auth.decorators.login_required






