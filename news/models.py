from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    # class Meta:
    #     # verbose_name = 'Титул'  # как обратится к модели
    #     # verbose_name_plural = 'Титулы'
    #     db_table = 'users'
    #     indexes = [models.Index(fields=['login'])]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def created_date(self):
        return self.user.date_joined

    def __repr__(self):
        return f'{self.user.first_name}'

    def __str__(self):
        return f'{self.user.username} - {", ".join(x.name for x in  self.user.groups.all())}'


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        unique_together = ['title', 'category']
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=False)
    category = models.ForeignKey(Category,
                                    on_delete=models.CASCADE,
                                    null=False,
                                    blank=False)
    title = models.CharField(max_length=256,
                             unique=True,
                             null=False,
                             blank=False)
    content = models.TextField(null=False,
                               blank=False)
    created_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category_id}: {self.title[:32]}'


class Comments(models.Model):
    """https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name"""
    class Meta:
        unique_together = ['users_id', 'news_id', 'content']
        ordering = ['created_date']
    users_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="comments",
                                 related_query_name="comments",
                                 )
    news_id = models.ForeignKey(News, on_delete=models.CASCADE,
                                related_name="comments",
                                related_query_name="comments",
    )
    content = models.TextField(max_length=512)
    created_date = models.DateTimeField(default=datetime.now)
