from django import forms
from news.models import Comments


# Create the form class.
class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['content', 'news_id', 'users_id']

