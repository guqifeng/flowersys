# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
    ]
