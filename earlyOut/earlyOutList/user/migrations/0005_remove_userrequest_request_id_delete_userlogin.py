# Generated by Django 4.2.1 on 2023-05-24 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_user_id_userrequest_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrequest',
            name='request_id',
        ),
        migrations.DeleteModel(
            name='UserLogin',
        ),
    ]
