from django.contrib.auth.models import User, Group
from rest_framework import serializers

from news.models import News, Category, Comments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'url', 'first_name', 'last_name', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'url', 'name')


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('pk', 'user', 'category', 'title', 'content', 'created_date', 'is_published', 'comments')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name',)


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('pk', 'users', 'news', 'content', 'created_date')
