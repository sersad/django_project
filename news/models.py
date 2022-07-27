from datetime import datetime

from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UsersTypes(models.Model):
    users_type = models.CharField(max_length=32)

    def __repr__(self):
        return f"***\n<class={__class__.__name__}>\n" \
               f"id={self.id}\tusers_type={self.users_type}\t" \
               f"\n***"


class Users(models.Model):
    name = models.CharField(max_length=32)
    login = models.CharField(max_length=32,
                             unique=True)
    email = models.EmailField(db_index=True,
                              unique=True)
    user_type_id = models.ForeignKey(UsersTypes, on_delete=models.CASCADE)
    hashed_password = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now)

    # устанавливает значение хэша пароля для переданной строки.
    # для регистрации пользователя
    def set_password(self, password):
        self.hashed_password = make_password(password)

    # правильный ли пароль ввел пользователь
    # авторизация пользователей
    def check_password(self, password):
        return check_password(password, self.hashed_password)

    def __repr__(self):
        return f"***\n<class={__class__.__name__}>\n" \
               f"id={self.id}\tname={self.name}\tlogin={self.login}\temail={self.email}\tcreated_date={self.created_date}\n" \
               f"hashed_password={self.hashed_password}" \
               f"\n***"


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __repr__(self):
        return f"***\n<class={__class__.__name__}>\n" \
               f"name={self.name}" \
               f"\n***"


class News(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __repr__(self):
        return f"***\n<class={__class__.__name__}>\n" \
               f"id={self.id}\ttitle={self.title}\tcontent={self.content}\tuser_id={self.user_id} " \
               f"created_date={self.created_date}\tis_published={self.is_published} " \
               f"\n***"


class Comments(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    created_date = models.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f"***\n<class={__class__.__name__}>\n" \
               f"id={self.id}\tusers_id={self.users_id}\tnews_id={self.news_id}" \
               f"content={self.content}\tcreated_date={self.created_date}" \
               f"\n***"
