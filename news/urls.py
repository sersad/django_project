from django.urls import path
from .views import *

urlpatterns = [
    # path('<int:category_id>', index, name='index'),
    # path('', index, name='index'),
    path('<int:category_id>', IndexListView.as_view(), name='index'),
    path('', IndexListView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('category', CategoryCreateView.as_view(), name='category'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('news', NewsCreateView.as_view(), name='news'),
]


