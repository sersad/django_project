from django.urls import path
from .views import *

urlpatterns = [
    path('<int:category_id>', index, name='index'),
    path('', index, name='index'),
    path('hello', hello, name='hello'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('category', CategoryCreateView.as_view(), name='category'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
]


