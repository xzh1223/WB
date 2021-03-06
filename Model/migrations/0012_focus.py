# Generated by Django 2.2 on 2019-01-16 04:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0011_myblog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('time', models.IntegerField(default=0, null=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
