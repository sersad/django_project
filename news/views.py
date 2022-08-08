from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView, UpdateView, FormView
from django.views.generic.edit import FormMixin, ModelFormMixin

from .forms import CommentsForm, NewsForm, UserForm, NewUserForm
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
        # определяем редактора
        context['is_admin'] = self.request.user.groups.filter(name='Editor').exists()
        return context


class IndexListView(CategoriesMixin, ListView, FormView):
    """
    Основная страничка новостей
    """
    model = News
    template_name = 'index.html'
    context_object_name = 'news'  # human-understandable name of variable to access from templates
    category_id = 0  # категория по умолчанию все (0)

    form_class = CommentsForm

    success_url = reverse_lazy('index')

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
        context['form'] = self.get_form()
        return context

    def get_form(self, form_class=None):
        """
        Магия для того чтоб форма добавить атрибуты
        """
        if form_class is None:
            form_class = self.get_form_class()

        form = super(IndexListView, self).get_form(form_class)
        form.fields['content'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'form-content',
            'placeholder': 'Enter comment'
        })
        return form

    def form_valid(self, form):
        """
        замена post(self, request, *args, **kwargs)
        :param form:
        :return:
        """
        form.instance.save()
        return super().form_valid(form)

    # можно или form_valid или как ниже для примера, оставлено на память
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         # print(form.cleaned_data)
    #         form.save()
    #         return HttpResponseRedirect(reverse('index'))
    #     # print('form invalid', form.cleaned_data)
    #     return self.get(request)


class AboutView(CategoriesMixin, TemplateView):
    template_name = "about.html"


class ContactsView(CategoriesMixin, TemplateView):
    template_name = "contacts.html"


class CategoriesListView(LoginRequiredMixin, CategoriesMixin, ListView):
    """
    Просмотр категорий новостей
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
    TODO: Generic Destroy API View generics.DestroyAPIView
    """
    model = Category
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('categories')


class CategoryUpdateView(LoginRequiredMixin, CategoriesMixin, UpdateView):
    """
    Обрабатывает Обновление категории
    """
    model = Category
    fields = ['name']
    template_name = 'category.html'
    success_url = reverse_lazy('categories')

    # можно в миксин для определения типа пользователя CategoriesMixin
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)


class NewsUpdateView(LoginRequiredMixin, CategoriesMixin, UpdateView):
    """
    Создание новой категории
    TODO: еще не написано
    """
    model = News
    form_class = NewsForm
    template_name = 'news.html'
    success_url = reverse_lazy('index')


class NewsCreateView(LoginRequiredMixin, CategoriesMixin, CreateView):
    """
    Создание новостей
    """
    model = News
    template_name = 'news.html'
    form_class = NewsForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        print(form.errors)

    # def post(self, request, *args, **kwargs):
    #     request.POST = request.POST.copy()
    #     request.POST['user_id'] = request.user.id
    #     return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        замена post(self, request, *args, **kwargs)
        :param form:
        :return:
        """
        form.instance.user = self.request.user
        # form.instance.save()
        return super().form_valid(form)


class NewsDeleteView(LoginRequiredMixin, CategoriesMixin, DeleteView):
    """
    Удаление новости
    """
    model = News
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('index')


class UsersListView(LoginRequiredMixin, CategoriesMixin, ListView):
    """
    Просмотр пользователей
    TODO: переписать это context_object_name = 'category' на mixin CategoriesMixin и поменять шаблон
    """
    login_url = 'login'  # если не авторизован, то кинем на авторизацию
    redirect_field_name = 'users'  # при каких либо действиях редирект обратно (не уверен, что это нужно)
    model = User
    context_object_name = 'users'  # c каким именем идет context
    template_name = 'users.html'  # имя шаблона


class UserUpdateView(LoginRequiredMixin, CategoriesMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user.html'
    success_url = reverse_lazy('users')


class UsersDeleteView(LoginRequiredMixin, CategoriesMixin, DeleteView):
    """
    Обрабатывает удаление пользователя
    """
    model = Users
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('users')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})