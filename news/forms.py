from django import forms

from news.models import Comments, News, Category


# Create the form class.
class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['content', 'news_id', 'users_id']


# Create the form class.
class NewsForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset=Category.objects.all())

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