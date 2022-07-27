from django.urls import path
from .views import hello

urlpatterns = {
    # path('', main, name='main'),
    path('hello', hello, name='hello'),
}


