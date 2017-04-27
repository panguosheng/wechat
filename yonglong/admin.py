# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import *


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('heading', )
    list_filter = ('heading', )


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'QQ', 'Email')
    list_filter = ('name',)


class BusRouteAdmin(admin.ModelAdmin):
    list_display = ('station', )


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('post', 'ship_type', 'area', 'remark')
    list_filter = ('post',)
    search_fields = ('post', 'remark')
    date_hierarchy = 'issue_date'
    fieldsets = [
        ('船舶信息', {'fields': [
            'ship_name',
            'ship_type',
            'area',
            'load',
            'flag',
            'line',
            'line_start',
            'line_end',
            'engine_type',
            'power',
            'operative',
        ]}),
        ('职位描述', {'fields': [
            'post',
            'certificate_grade',
            'certificate_special',
            'work_years',
            'issue_date',
            'deadline',
            'on_board_time',
            'on_board_address',
            'contract',
        ]}),
        ('备注信息', {'fields': ['remark', ]}),
        ('联系信息', {'fields': ['contacts', ]})
    ]


class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'category',)
    list_filter = ('category',)
    date_hierarchy = 'pub_date'

    class Media:
        # 在管理后台的HTML文件中加入js文件，每一个路径都会追加STATIC_URL/
        js = (
            'yonglong/js/kindeditor-4.1.7/kindeditor-all.js',
            'yonglong/js/kindeditor-4.1.7/lang/zh_CN.js',
            'yonglong/js/kindeditor-4.1.7/config.js',
        )


class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'category_cn')


class AboutAdmin(admin.ModelAdmin):
    class Media:
        # 在管理后台的HTML文件中加入js文件，每一个路径都会追加STATIC_URL/
        js = (
            'yonglong/js/kindeditor-4.1.7/kindeditor-all.js',
            'yonglong/js/kindeditor-4.1.7/lang/zh_CN.js',
            'yonglong/js/kindeditor-4.1.7/config.js',
        )


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_cn', 'post_en',)
    ordering = ('id',)


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('title', )

    class Media:
        # 在管理后台的HTML文件中加入js文件，每一个路径都会追加STATIC_URL/
        js = (
            'yonglong/js/kindeditor-4.1.7/kindeditor-all.js',
            'yonglong/js/kindeditor-4.1.7/lang/zh_CN.js',
            'yonglong/js/kindeditor-4.1.7/config.js',
        )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Media:
        # 在管理后台的HTML文件中加入js文件，每一个路径都会追加STATIC_URL/
        js = (
            'yonglong/js/kindeditor-4.1.7/kindeditor-all.js',
            'yonglong/js/kindeditor-4.1.7/lang/zh_CN.js',
            'yonglong/js/kindeditor-4.1.7/config.js',
        )


class CrewAppearanceAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category', 'pub_time')
    list_filter = ('category',)
    date_hierarchy = 'pub_time'

admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(BusRoute, BusRouteAdmin)
admin.site.register(Employment, EmploymentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CertificateGrade)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CrewAppearance, CrewAppearanceAdmin)
