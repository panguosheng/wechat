# -*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Certificate, Contacts, BusRoute, Employment, News, \
    About, Post, NewsCategory, Business, Partner, CrewAppearance

COMPANY_PURPOSE = '以人为本、以德为先、德才兼备'

page_size = 10
after_range_num = 6
before_range_num = 5


def index(request):
    employment_list = Employment.objects.all().order_by('-id')[0:5]
    news_list = News.objects.values('id', 'headline').order_by('-id')[0:5]
    partner_list = Partner.objects.values('name')[0:5]
    appearance_list = CrewAppearance.objects.all()[0:9]
    content = {
        'active_menu': 'index',
        'employment_list': employment_list,
        'news_list': news_list,
        'partner_list': partner_list,
        'login_user': request.user,
        'appearance_list': appearance_list,
    }
    return render(request, 'yonglong/index.html', content)


def about(request):
    """关于我们"""
    about_content = get_object_or_404(About, pk=1)
    content = {
        'active_menu': 'about',
        'company_purpose': COMPANY_PURPOSE,
        'about': about_content,
        'login_user': request.user,
    }
    return render(request, 'yonglong/about.html', content)


def business(request):
    """公司业务范围"""
    business_list = Business.objects.all()
    content = {
        'active_menu': 'business',
        'company_purpose': COMPANY_PURPOSE,
        'business_list': business_list,
        'login_user': request.user,
    }
    return render(request, 'yonglong/business.html', content)


def certificate(request):
    """可办理的证件"""
    certificate_list = Certificate.objects.all()
    content = {
        'active_menu': 'certificate',
        'company_purpose': COMPANY_PURPOSE,
        'certificate_list': certificate_list,
        'login_user': request.user,
    }
    return render(request, 'yonglong/certificate.html', content)


def certificate_details(request, certificate_id):
    """办证详细信息"""
    detail = get_object_or_404(Certificate, pk=certificate_id)
    content = {
        'active_menu': 'certificate',
        'company_purpose': COMPANY_PURPOSE,
        'certificate': detail,
        'login_user': request.user,
    }
    return render(request, 'yonglong/certificate_details.html', content)


def contact(request):
    """公司联系人"""
    contact_list = Contacts.objects.all()
    bus_route_list = BusRoute.objects.all()
    content = {
        'active_menu': 'contact',
        'company_purpose': COMPANY_PURPOSE,
        'contact_list': contact_list,
        'bus_route_list': bus_route_list,
        'login_user': request.user,
    }
    return render(request, 'yonglong/contact.html', content)


def baidu_map(request):
    """百度地图"""
    return render(request, 'yonglong/map.html')


def news(request):
    """新闻页"""
    category_cn_dict = {}  # 字典用于存放类别英文与中文键值对
    category_index_dict = {}  # 字典用于存放类别英文与id键值对
    # 取得新闻类别
    category_list = NewsCategory.objects.all()

    for item in category_list:
        category_cn_dict[item.category] = item.category_cn
        category_index_dict[item.category] = item.id

    news_headline = ''
    if request.method == 'GET':
        try:
            query = request.GET['category']
            if query != 'all':
                q_set = (
                    Q(category=category_index_dict[query])
                )
                news_headline = category_cn_dict[query]
                results = News.objects.filter(q_set).order_by('-id')
            else:
                results = News.objects.values('id', 'headline', 'pub_date').order_by('-id')
        except Exception as e:
            # 如果没有？type=参数时执行
            query = 'all'  # 第一次打开时，没有query参数，
            news_headline = '新闻动态'
            results = News.objects.values('id', 'headline', 'pub_date').order_by('-id')

        try:
            page = int(request.GET.get("page", 1))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        paginator = Paginator(results, per_page=page_size)
        try:
            result_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            result_list = paginator.page(1)
        if page >= after_range_num:
            page_range = paginator.page_range[page - after_range_num:page + before_range_num]
        else:
            page_range = paginator.page_range[0:int(page) + before_range_num]

        content = {
            'active_menu': 'news',
            'active_category': query,
            'company_purpose': COMPANY_PURPOSE,
            'category_list': category_list,
            'info': result_list,
            'category': query,
            'news_headline': news_headline,
            'page_range': page_range,
            'error_msg': '没有相关信息',
            'login_user': request.user,
        }
        return render(request, 'yonglong/news.html', content)


def news_details(request, news_id):
    """通过news_id查询新闻详细信息"""
    detail = get_object_or_404(News, pk=news_id)
    # 每读一次，次数加一
    detail.times += 1
    detail.save()
    content = {
        'active_menu': 'news',
        'company_purpose': COMPANY_PURPOSE,
        'news': detail,
        'login_user': request.user,
    }
    return render(request, 'yonglong/news_details.html', content)


def employment(request):
    """船员招聘页"""
    quarters_list = Post.objects.all()
    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(Employment.objects.all().order_by('-id'), per_page=page_size)
    try:
        result_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        result_list = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + before_range_num]
    content = {
        'active_menu': 'employment',
        'post_list': quarters_list,
        'active_sidebar': 'all',
        'company_purpose': COMPANY_PURPOSE,
        'employment_list': result_list,
        'page_range': page_range,
        'error_msg': '没有相关信息',
        'login_user': request.user,
    }
    return render(request, 'yonglong/employment.html', content)


def employment_post(request, quarters):
    """船员招聘页"""
    quarters_dict = {}  # 空字典用于存放职位的英文和中文的键值对
    quarters_list = Post.objects.all()  # 查询出职位所对应的英文和中文

    for item in quarters_list:
        quarters_dict[item.post_en] = item.id

    if quarters == 'all':
        results = Employment.objects.all().order_by('-id')
    else:
        results = Employment.objects.filter(post=quarters_dict[quarters]).order_by('-id')

    try:
        page = int(request.GET.get("page", 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(results, per_page=page_size)
    try:
        result_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        result_list = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + before_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + before_range_num]
    content = {
        'active_menu': 'employment',
        'post_list': quarters_list,
        'active_sidebar': quarters,
        'company_purpose': COMPANY_PURPOSE,
        'employment_list': result_list,
        'page_range': page_range,
        'error_msg': '没有相关信息',
        'login_user': request.user,
    }
    return render(request, 'yonglong/employment.html', content)


def employment_details(request, employment_id):
    """招聘详细信息"""
    detail = Employment.objects.get(pk=employment_id)
    linkman = Contacts.objects.values('telephone', 'QQ').get(name=detail.contacts)
    content = {
        'active_menu': 'employment',
        'company_purpose': COMPANY_PURPOSE,
        'employ': detail,
        'linkman': linkman,
        'login_user': request.user,
    }
    return render(request, 'yonglong/employment_details.html', content)


def partner(request):
    """公司合作伙伴"""
    partner_content = Partner.objects.all()
    content = {
        'active_menu': 'partner',
        'company_purpose': COMPANY_PURPOSE,
        'partner_content': partner_content,
        'login_user': request.user,
    }
    return render(request, 'yonglong/partner.html', content)


def appearance(request):
    appearance_list = CrewAppearance.objects.all()
    content = {
        # 'active_menu': 'partner',
        'company_purpose': COMPANY_PURPOSE,
        'appearance_list': appearance_list,
        'login_user': request.user,
    }

    return render(request, 'yonglong/appearance.html', content)


def account_login(request):
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'yonglong/login.html', {})
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(request.session['login_from'])
        else:
            content = {
                'password_is_wrong': True,
                'current_name': username,
            }
            return render(request, 'yonglong/login.html', content)


@login_required
def account_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
