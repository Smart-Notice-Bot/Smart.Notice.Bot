# Generated by Django 3.2.5 on 2021-11-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='notice',
        ),
        migrations.AddField(
            model_name='user',
            name='employ',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='founded',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='graduate_school',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='intern',
            field=models.TextField(null=True),
        ),
    ]
