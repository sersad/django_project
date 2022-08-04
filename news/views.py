from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView

from .models import *


# Create your views here.


class CategoriesMixin:
    """
    Mixin для подгрузки категорий новостей. Используется для формирования левого меню.
    """

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class IndexListView(CategoriesMixin, ListView):
    """
    Основная страничка новостей
    """
    model = News
    template_name = 'index.html'
    context_object_name = 'news'  # human-understandable name of variable to access from templates
    category_id = 0  # категория по умолчанию все (0)

    def get_queryset(self):
        """
        Dynamic filtering https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
        """
        if not self.kwargs.get('category_id'):
            return News.objects.all()
        self.category_id = self.kwargs['category_id']
        return News.objects.filter(category_id=self.category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.category_id:
            title = "Последние новости"
        else:
            title, = [i.name for i in context['category'] if i.id == self.category_id]
        context['title'] = title  # формирование заголовка
        return context


class AboutView(CategoriesMixin, TemplateView):
    template_name = "about.html"


class ContactsView(CategoriesMixin, TemplateView):
    template_name = "contacts.html"


class CategoriesListView(LoginRequiredMixin, ListView):
    """
    Просмотр категорий новостей
    TODO: переписать это context_object_name = 'category' на mixin CategoriesMixin и поменять шаблон
    """
    login_url = 'login'  # если не авторизован, то кинем на авторизацию
    redirect_field_name = 'categories'  # при каких либо действиях редирект обратно (не уверен, что это нужно)
    model = Category
    context_object_name = 'category'  # c каким именем идет context
    template_name = 'categories.html'  # имя шаблона

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Просмотр категорий'
        return context


class CategoryCreateView(LoginRequiredMixin, CategoriesMixin, CreateView):
    """
    Создание новой категории
    """
    model = Category
    fields = ['name']
    template_name = 'category.html'

    def get_success_url(self):
        """
        Если все удачно, то вернем пользователя на categories
        """
        return reverse('categories')

    def get_form(self, form_class=None):
        """
        Магия для того чтоб форма добавить атрибуты
        """
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CategoryCreateView, self).get_form(form_class)
        form.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-control', 'type': 'form-name',
            'placeholder': 'Enter category Name'})
        return form


class CategoryDeleteView(LoginRequiredMixin, CategoriesMixin, DeleteView):
    """
    Обрабатывает удаление категории
    """
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('categories')


class CategoryUpdateView(LoginRequiredMixin, CategoriesMixin, UpdateView):
    """
    Обрабатывает Обновление категории
    """
    model = Category
    fields = ['name']
    template_name = 'category.html'
    success_url = reverse_lazy('categories')


class NewsCreateView(LoginRequiredMixin, CategoriesMixin, CreateView):
    """
    Создание новой категории
    TODO: еще не написано
    """
    model = News
    fields = ['title']
    template_name = 'news.html'

    def get_success_url(self):
        """
        Если все удачно, то вернем пользователя на заглавную
        """
        return reverse('')

    # def get_form(self, form_class=None):
    #     """
    #     Магия для того чтоб форма добавить атрибуты
    #     """
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #
    #     form = super(CategoryCreateView, self).get_form(form_class)
    #     form.fields['name'].widget = forms.TextInput(attrs={
    #         'class': 'form-control', 'type': 'form-name',
    #         'placeholder': 'Enter category Name'})
    #     return form


###СТАРЬЕ но тут нужная форма которую нужно перенести в IndexListView


def index(request, category_id=0):
    # form = CommentForm()
    if category_id != 0:
        news = News.objects.filter(category_id=category_id).order_by('created_date').all()
    else:
        news = News.objects.order_by('created_date').all()

    categories = Category.objects.all()
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
