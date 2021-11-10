from django import forms
from .models import Blog

class BlogUpdate(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
