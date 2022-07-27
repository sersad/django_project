
#### Описание
В директории `pg` находятся volume `postgres` и `pgadmin`
#### Запуск из корня 

`docker-compose up -d --build`

- django http://127.0.0.1:8000

- админка django http://127.0.0.1:8000/admin/

- pgadmin http://127.0.0.1:5050/browser/

#### Запуск команды migrate в контейнере
`docker-compose run web python manage.py migrate`

#### Создание супер пользователя root 
`docker-compose run web python manage.py createsuperuser`
пароль `123`

docker-compose run web python manage.py startapp news

загружаем фикстуры
docker-compose run web python manage.py loaddata fixtures/data


#### очистка всего старого в докере
`docker system prune -a -f`


Руководство Django Часть 8: Аутентификация и авторизация пользователя - Изучение веб-разработки 
https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Authentication