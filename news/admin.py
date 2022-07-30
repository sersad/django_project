from django.contrib import admin

# Register your models here.
from news.models import News, Users, Category, Comments

admin.site.register(News)
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Comments)
