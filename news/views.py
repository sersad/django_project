from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def hello(request):
    users_type = UsersTypes.objects.all()
    users = Users.objects.all()
    return HttpResponse("Hello")


# def main(request):
#     return render(request, "blog/index.html", {"user": request.user})
