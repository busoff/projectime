# Generated by Django 2.1.2 on 2018-12-08 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20181208_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
