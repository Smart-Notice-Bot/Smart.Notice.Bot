from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
from django import forms
# from . import models
...

class AdminType(object):
    USER = "user"
    ADMIN = "admin"

class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})

class User(AbstractBaseUser):
    username=models.TextField(unique=True)
    email=models.TextField(null=True)
    admin_type=models.TextField(default=AdminType.USER)
    dept=models.TextField(null=True)
    general=models.TextField(null=True)
    school=models.TextField(null=True)
    international=models.TextField(null=True)
    employ=models.TextField(null=True)
    scholarship=models.TextField(null=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def is_admin(self):
        return self.admin_type == AdminType.ADMIN

    class Meta:
        db_table = "user"


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) # 👈 Password로 템플릿에 필드가 표시됩니다.
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password") # 👈 label값으로 템플릿에 필드가 표시됩니다.