# Generated by Django 2.2 on 2018-12-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0008_myblog_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='user_id',
        ),
    ]
