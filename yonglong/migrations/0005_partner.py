# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonglong', '0004_auto_20170422_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='公司名称')),
                ('name_en', models.CharField(blank=True, max_length=200, verbose_name='公司名称英文')),
                ('logo', models.ImageField(blank=True, upload_to='yonglong/logo/', verbose_name='公司logo')),
                ('content', models.TextField(blank=True, verbose_name='公司介绍')),
            ],
            options={
                'verbose_name': '合作伙伴',
                'verbose_name_plural': '合作伙伴',
            },
        ),
    ]
