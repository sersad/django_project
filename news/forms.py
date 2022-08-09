from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

from news.models import Comments, News


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'news', 'users']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category', 'title', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'size': 80,
                'type': 'form-title',
                'placeholder': 'Enter News title'}),
            'content': forms.Textarea(attrs={
                'cols': 100,
                'rows': 50,
                'placeholder': 'Enter News here'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-control',
                'placeholder': 'Enter your First Name'}),
            'last_name': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-control',
                'placeholder': 'Enter your Last Name'}),
            'username': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-title',
                'placeholder': 'Enter your Login'}),
            'email': forms.TextInput(attrs={
                'size': 28,
                'type': 'email',
                'placeholder': 'Enter your Email'}),
            'groups': forms.SelectMultiple(attrs={
                'size': 2,
                'type': 'email',
                'placeholder': 'Choice group'}),

        }


class NewUserForm(UserCreationForm):
    """
    https://django.fun/docs/django/ru/4.0/ref/contrib/messages/
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-control',
                'placeholder': 'Enter your First Name'}),
            'last_name': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-control',
                'placeholder': 'Enter your Last Name'}),
            'username': forms.TextInput(attrs={
                'size': 28,
                'type': 'form-title',
                'placeholder': 'Enter your Login'}),
            'email': forms.TextInput(attrs={
                'size': 28,
                'type': 'email',
                'placeholder': 'Enter your Email'}),

        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        group = Group.objects.get(name='Reader')
        if commit:
            user.save()
            user.groups.add(group)
        return user


