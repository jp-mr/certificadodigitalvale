# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0003_auto_20161129_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ecpf',
            options={'ordering': ['posição'], 'verbose_name_plural': 'e-CPF'},
        ),
        migrations.AlterModelOptions(
            name='nfe',
            options={'ordering': ['posição'], 'verbose_name_plural': 'NF-e'},
        ),
    ]
