# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-20 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=20, verbose_name='公司简介')),
                ('content', models.TextField(blank=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '公司简介',
                'verbose_name_plural': '公司简介',
            },
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(blank=True, max_length=50, verbose_name='站点')),
                ('route', models.TextField(blank=True, verbose_name='线路')),
            ],
            options={
                'verbose_name': '乘车线路',
                'ordering': ['id'],
                'verbose_name_plural': '乘车线路',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50, verbose_name='名称')),
                ('pic', models.FileField(blank=True, upload_to='yonglong/certificate/', verbose_name='图片')),
                ('details', models.TextField(blank=True, verbose_name='详细')),
            ],
            options={
                'verbose_name': '证书服务',
                'verbose_name_plural': '证书服务',
            },
        ),
        migrations.CreateModel(
            name='CertificateGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=20, verbose_name='证书等级')),
            ],
            options={
                'verbose_name': '证书等级',
                'verbose_name_plural': '证书等级',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('telephone', models.CharField(blank=True, max_length=15, verbose_name='电话')),
                ('QQ', models.CharField(blank=True, max_length=15, verbose_name='QQ')),
                ('Email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('zipcode', models.CharField(blank=True, max_length=6, verbose_name='邮编')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='地址')),
            ],
            options={
                'verbose_name': '联系人',
                'ordering': ['id'],
                'verbose_name_plural': '联系人',
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_name', models.CharField(blank=True, max_length=20, verbose_name='船名')),
                ('ship_type', models.CharField(blank=True, max_length=20, verbose_name='船型')),
                ('area', models.CharField(blank=True, max_length=20, verbose_name='航区')),
                ('load', models.CharField(blank=True, max_length=20, verbose_name='载重吨')),
                ('flag', models.CharField(blank=True, max_length=50, verbose_name='船旗')),
                ('line', models.CharField(blank=True, max_length=50, verbose_name='航线')),
                ('line_start', models.CharField(blank=True, max_length=50, verbose_name='航线起点')),
                ('line_end', models.CharField(blank=True, max_length=50, verbose_name='航线终点')),
                ('engine_type', models.CharField(blank=True, max_length=20, verbose_name='机型')),
                ('power', models.IntegerField(blank=True, null=True, verbose_name='功率')),
                ('operative', models.DateField(blank=True, null=True, verbose_name='下水时间')),
                ('certificate_special', models.CharField(blank=True, max_length=20, verbose_name='特殊证书')),
                ('work_years', models.IntegerField(blank=True, null=True, verbose_name='船龄')),
                ('issue_date', models.DateField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='截止日期')),
                ('on_board_time', models.DateField(blank=True, null=True, verbose_name='上船时间')),
                ('on_board_address', models.CharField(blank=True, max_length=50, verbose_name='上船地点')),
                ('contract', models.IntegerField(blank=True, null=True, verbose_name='合同期')),
                ('remark', models.CharField(blank=True, max_length=200, verbose_name='备注')),
                ('certificate_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yonglong.CertificateGrade', verbose_name='证书等级')),
                ('contacts', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='yonglong.Contacts', verbose_name='联系人')),
            ],
            options={
                'verbose_name': '招聘人员',
                'ordering': ['-id'],
                'verbose_name_plural': '招聘人员',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50, verbose_name='新闻标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('pic', models.FileField(blank=True, upload_to='yonglong/news_photos/', verbose_name='新闻图片')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('times', models.IntegerField(default=0, verbose_name='阅读次数')),
            ],
            options={
                'verbose_name': '新闻动态',
                'verbose_name_plural': '新闻动态',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='分类_英文')),
                ('category_cn', models.CharField(max_length=20, verbose_name='分类_中文')),
            ],
            options={
                'verbose_name': '新闻分类',
                'verbose_name_plural': '新闻分类',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_en', models.CharField(blank=True, max_length=20, verbose_name='职位英文')),
                ('post_cn', models.CharField(blank=True, max_length=20, verbose_name='职位中文')),
            ],
            options={
                'verbose_name': '职位名称',
                'verbose_name_plural': '职位名称',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='yonglong.NewsCategory', verbose_name='新闻类别'),
        ),
        migrations.AddField(
            model_name='employment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yonglong.Post', verbose_name='职位'),
        ),
    ]
