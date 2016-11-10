# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import tabela.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecnpj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=tabela.models.upload_location)),
                ('modelo', models.CharField(max_length=80)),
                ('bloco_vermelho_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_vermelho_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_preço', models.CharField(blank=True, max_length=80)),
                ('posição', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['posição'],
                'verbose_name_plural': 'e-CNPJ',
            },
        ),
        migrations.CreateModel(
            name='Ecpf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=tabela.models.upload_location)),
                ('modelo', models.CharField(max_length=80)),
                ('bloco_vermelho_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_vermelho_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_preço', models.CharField(blank=True, max_length=80)),
                ('posição', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['posição'],
                'verbose_name_plural': 'e-CPF',
            },
        ),
        migrations.CreateModel(
            name='NFe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to=tabela.models.upload_location)),
                ('modelo', models.CharField(max_length=80)),
                ('bloco_vermelho_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_vermelho_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_verde_preço', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_validade', models.CharField(blank=True, max_length=80)),
                ('bloco_azul_preço', models.CharField(blank=True, max_length=80)),
                ('posição', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ['posição'],
                'verbose_name_plural': 'NF-e',
            },
        ),
    ]