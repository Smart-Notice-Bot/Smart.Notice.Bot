# Generated by Django 3.2.5 on 2021-11-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notice',
            field=models.JSONField(null=True),
        ),
    ]