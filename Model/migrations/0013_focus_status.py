# Generated by Django 2.2 on 2019-01-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0012_focus'),
    ]

    operations = [
        migrations.AddField(
            model_name='focus',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
