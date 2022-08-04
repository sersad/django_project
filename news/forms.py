from django.forms import ModelForm
from news.models import Comments


# Create the form class.
class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
