# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('url', models.URLField(verbose_name='URL')),
                ('name', models.CharField(max_length=1024, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('source', models.CharField(choices=[('pythondigest', 'pythondigest')], max_length=32, verbose_name='Источник')),
                ('external_id', models.CharField(blank=True, editable=False, max_length=32, null=True, unique=True, verbose_name='Внешний ID')),
                ('image', models.ImageField(blank=True, upload_to='articles', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Показывать на сайте')),
            ],
            options={
                'ordering': ['-published_at', '-id'],
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
