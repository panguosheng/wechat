# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonglong', '0002_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='业务标题'),
        ),
        migrations.AlterField(
            model_name='business',
            name='content',
            field=models.TextField(verbose_name='项目明细'),
        ),
    ]
