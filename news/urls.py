from django.urls import path
from .views import *

urlpatterns = [
    path('<int:category_id>', index, name='index'),
    path('', index, name='index'),
    path('hello', hello, name='hello'),
    path('categories', CategoriesListView.as_view()),
    path('category', CategoryCreateView.as_view()),
]


