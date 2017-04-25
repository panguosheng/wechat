# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """各个职位"""
    post_en = models.CharField(max_length=20, verbose_name='职位英文', blank=True)
    post_cn = models.CharField(max_length=20, verbose_name='职位中文', blank=True)

    class Meta:
        verbose_name = "职位名称"
        verbose_name_plural = "职位名称"

    def __str__(self):
        return self.post_cn


class CertificateGrade(models.Model):
    """证书各等级航区"""
    grade = models.CharField(max_length=20, verbose_name='证书等级')

    class Meta:
        verbose_name = "证书等级"
        verbose_name_plural = "证书等级"

    def __str__(self):
        return self.grade


class Certificate(models.Model):
    """ 公司办理证书服务 """
    heading = models.CharField(max_length=50, verbose_name='名称')
    pic = models.FileField(upload_to='yonglong/certificate/', blank=True, verbose_name='图片')
    details = models.TextField(blank=True, verbose_name='详细')

    class Meta:
        verbose_name = '证书服务'
        verbose_name_plural = '证书服务'

    def __str__(self):
        return self.heading


class About(models.Model):
    """ 公司简介"""
    headline = models.CharField(max_length=20, verbose_name='公司简介')
    content = models.TextField(verbose_name='内容', blank=True)

    class Meta:
        verbose_name = '公司简介'
        verbose_name_plural = '公司简介'

    def __str__(self):
        return self.headline


class Contacts(models.Model):
    """ 公司联系人信息 """
    name = models.CharField(max_length=50, verbose_name='姓名')
    telephone = models.CharField(max_length=15, verbose_name='电话', blank=True)
    QQ = models.CharField(max_length=15, verbose_name='QQ', blank=True)
    Email = models.EmailField(max_length=50, verbose_name='Email', blank=True)
    zipcode = models.CharField(max_length=6, verbose_name='邮编', blank=True)
    address = models.CharField(max_length=100, verbose_name='地址', blank=True)

    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'
        ordering = ['id']

    def __str__(self):
        return self.name


class BusRoute(models.Model):
    """ 来公司乘车线路 """
    station = models.CharField(max_length=50, verbose_name='站点', blank=True)
    route = models.TextField(verbose_name='线路', blank=True)

    class Meta:
        verbose_name = '乘车线路'
        verbose_name_plural = '乘车线路'
        ordering = ['id']

    def __str__(self):
        return self.station


class Employment(models.Model):
    """ 公司招聘人员 """
    # 船舶信息
    ship_name = models.CharField(max_length=20, verbose_name='船名', blank=True)
    ship_type = models.CharField(max_length=20, verbose_name='船型', blank=True)
    area = models.CharField(max_length=20, verbose_name='航区', blank=True)
    load = models.CharField(max_length=20, verbose_name='载重吨', blank=True)
    flag = models.CharField(max_length=50, verbose_name='船旗', blank=True)
    line = models.CharField(max_length=50, verbose_name='航线', blank=True)
    line_start = models.CharField(max_length=50, verbose_name='航线起点', blank=True)
    line_end = models.CharField(max_length=50, verbose_name='航线终点', blank=True)
    engine_type = models.CharField(max_length=20, verbose_name='机型', blank=True)
    power = models.IntegerField(verbose_name='功率', blank=True, null=True)
    operative = models.DateField(verbose_name='下水时间', blank=True, null=True)
    # 职位描述
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='职位')
    certificate_grade = models.ForeignKey(CertificateGrade, on_delete=models.CASCADE, verbose_name='证书等级')
    certificate_special = models.CharField(max_length=20, verbose_name='特殊证书', blank=True)
    work_years = models.IntegerField(verbose_name='船龄', blank=True, null=True)
    issue_date = models.DateField(verbose_name='发布日期', auto_now=False, default=timezone.now)
    deadline = models.DateField(verbose_name='截止日期', auto_now=False, blank=True, null=True)
    on_board_time = models.DateField(verbose_name='上船时间', blank=True, null=True)
    on_board_address = models.CharField(max_length=50, verbose_name='上船地点', blank=True)
    contract = models.IntegerField(verbose_name='合同期', blank=True, null=True)
    # 备注信息
    remark = models.CharField(max_length=200, verbose_name='备注', blank=True)
    # 联系信息
    contacts = models.ForeignKey(Contacts, default=2, verbose_name='联系人', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '招聘人员'
        verbose_name_plural = '招聘人员'
        ordering = ['-id']

    def __str__(self):
        return self.post.post_cn


class NewsCategory(models.Model):
    """新闻分类"""
    category = models.CharField(max_length=20, verbose_name='分类_英文')
    category_cn = models.CharField(max_length=20, verbose_name='分类_中文')

    class Meta:
        verbose_name = '新闻分类'
        verbose_name_plural = '新闻分类'

    def __str__(self):
        return self.category_cn


class News(models.Model):
    """ 新闻动态 """
    headline = models.CharField(max_length=50, verbose_name='新闻标题')
    content = models.TextField(verbose_name='内容')
    pic = models.FileField(verbose_name='新闻图片', upload_to='yonglong/news_photos/', blank=True)
    pub_date = models.DateTimeField(verbose_name='发布时间', default=timezone.now)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='新闻类别', default=1)
    times = models.IntegerField(verbose_name='阅读次数', default=0)

    class Meta:
        verbose_name = '新闻动态'
        verbose_name_plural = '新闻动态'

    def __str__(self):
        return self.headline


class Business(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'业务标题', blank=True)
    content = models.TextField(verbose_name=u'项目明细', blank=True)

    class Meta:
        verbose_name = u'业务范围'
        verbose_name_plural = u'业务范围'

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'公司名称')
    name_en = models.CharField(max_length=200, verbose_name=u'公司名称英文', blank=True)
    logo = models.ImageField(upload_to='yonglong/logo/', verbose_name=u'公司logo', blank=True)
    content = models.TextField(verbose_name=u'公司介绍', blank=True)

    class Meta:
        verbose_name = u'合作伙伴'
        verbose_name_plural = u'合作伙伴'

    def __str__(self):
        return self.name


class CrewAppearance(models.Model):
    headline = models.CharField(max_length=100, verbose_name='图片描述')
    picture = models.ImageField(upload_to='yonglong/appearance/', verbose_name='图片')

    class Meta:
        verbose_name = u'船员风采'
        verbose_name_plural = u'船员风采'

    def __str__(self):
        return self.headline
