# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20161204_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ecnpj',
            options={'ordering': ['-id'], 'verbose_name_plural': 'e-CNPJ'},
        ),
    ]
