from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .models import *


# Create your views here.


def hello(request):

    return HttpResponse("Hello")


# def main(request):
#     return render(request, "blog/index.html", {"user": request.user})

def index(request, category_id=0):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    # num_books=Book.objects.all().count()
    # num_instances=BookInstance.objects.all().count()
    # # Доступные книги (статус = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # form = CommentForm()
    if category_id != 0:
        news = News.objects.filter(category_id=category_id).order_by('created_date').all()
    else:
        news = News.objects.order_by('created_date').all()

    categories = Category.objects.all()
    title = "Последние новости"
    if not category_id:
        title = "Последние новости"
    else:
        title, = [i.name for i in categories if i.id == category_id]
    # if form.validate_on_submit():
    #     comment = Comments(content=form.content.data,
    #                        users_id=current_user.id,
    #                        news_id=int(form.news_id.data))
    #     db_sess.add(comment)
    #     db_sess.commit()
    #     return redirect(f"/{category_id}")
    return render(request,
                  'index.html',
                  context={'news': news,
                           # 'form': form,
                           'category': categories,
                           'title': title})

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    # return render(
    #     request,
    #     'index.html',
    #     context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    # )


class CategoriesListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'categories'
    model = Category
    context_object_name = 'category'
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = 'Просмотр категорий'
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'category.html'

    def get_success_url(self):
        return reverse('categories')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CategoryCreateView, self).get_form(form_class)
        form.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control', 'type': 'form-name',
            'placeholder': 'Enter category Name'})
        return form


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
