from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #form of model Post
        fields = ('title', 'text',) #input fields of form
