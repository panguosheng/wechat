from django.conf.urls import url
from .views import index, about, certificate, contact, certificate_details, baidu_map, news, news_details, employment, \
    employment_post, business, employment_details, partner, account_login, account_logout, appearance

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^certificate/$', certificate, name='certificate'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^business/$', business, name='business'),
    url(r'^certificate_details/(?P<certificate_id>\d+)/$', certificate_details, name='certificate_details'),
    url(r'^baidu_map/$', baidu_map, name='baidu_map'),
    url(r'^news/', news, name='news'),
    url(r'^news_details/(?P<news_id>\d+)/$', news_details, name='news_details'),
    url(r'^employment/$', employment, name='employment'),
    url(r'^employment/(?P<quarters>.+)/$', employment_post, name='employment_post'),
    url(r'^employment_detail/(?P<employment_id>\d+)/$', employment_details, name='employment_details'),
    url(r'^partner/$', partner, name='partner'),
    url(r'^appearance/$', appearance, name='appearance'),
    url(r'^accounts/login/$', account_login, name='login'),
    url(r'^accounts/logout/$', account_logout, name='logout'),
]
