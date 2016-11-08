# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecpf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=80)),
                ('descrição', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'e-CPF',
            },
        ),
        migrations.CreateModel(
            name='NFe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=80)),
                ('descrição', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'NF-e',
            },
        ),
    ]
