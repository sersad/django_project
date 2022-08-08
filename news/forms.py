from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        fields = ['first_name', 'username', 'email', 'groups']


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        group = Group.objects.get(name='Reader')
        if commit:
            user.save()
            user.groups.add(group)
        return user