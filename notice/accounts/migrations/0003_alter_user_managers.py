# Generated by Django 3.2.5 on 2021-11-26 12:12

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
