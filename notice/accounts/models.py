from django.db import models

# Create your models here.
from django import forms
from . import models
...
class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) # 👈 Password로 템플릿에 필드가 표시됩니다.
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password") # 👈 label값으로 템플릿에 필드가 표시됩니다.