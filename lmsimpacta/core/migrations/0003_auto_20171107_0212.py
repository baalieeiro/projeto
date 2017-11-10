# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171107_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='carga_horaria',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]