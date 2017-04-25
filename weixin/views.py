#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,HttpResponseBadRequest

from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf,WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage,VoiceMessage,ShortVideoMessage,VideoMessage,ImageMessage,LinkMessage
from wechat_sdk.messages import LocationMessage,EventMessage

from .reply_text import doreply

# Create your views here.

TOKEN = 'weixin_pan'
APPID = 'wxc0ed3cb9d99969c5'
APPSECRET = '932d14e9bd799ca8b680e0702845bb1b'
ENCODING_AES_KEY = 'Qx8zoGFo9Czwf7zidLJTASXrneNWzmkUpk8RhohC4vU'

# 实例化WechatConf配置类
conf = WechatConf(
    token=TOKEN,
    appid = APPID,
    appsecret=APPSECRET,

    # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全模式
    encrypt_mode='compatible',

    # 如果传入此值则必须保证同时传入token,appid
    encoding_aes_key=ENCODING_AES_KEY,
)

# 实例化WeChatBasic类
wechat = WechatBasic(conf)


@csrf_exempt
def index_weixin(request):
    """
        所有的消息都会先进入这个函数进行处理，函数包含两个功能，
        微信接入验证是GET方法，
        微信正常的收发消息是用POST方法。
        """

    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature','')
        timestamp = request.GET.get('timestamp','')
        nonce =  request.GET.get('nonce','')
        echo_str = request.GET.get('echostr','')

        if not wechat.check_signature(signature=signature,timestamp=timestamp,nonce=nonce):
            return HttpResponseBadRequest('Verify Faild')

        return HttpResponse(echo_str,content_type="text/plain")

    else:
        # request.method == 'POST'
        # 解析本次请求的 XML 数据
        try:
            wechat.parse_data(request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')

        # 获取解析好的微信请求信息
        message = wechat.get_message()
        # 利用本次请求中的用户OpenID来初始化上下文对话
        # content = DatabaseContextStore(openid=message.source)

        if isinstance(message,TextMessage):
            # 当前会话次数，如果没有则返回1
            # step = content.get('step',1)
            # 当前会话内容
            content = message.content.strip()
            if content == '功能':
                translation = '1.中英文翻译，用法：翻译两字后跟所翻译内容'
                jok = '2.开心一刻，用法：输入笑话'
                book = '3.图书，用法：图书两字后跟图书名'
                reply = '%s\n%s\n%s\n' % (translation, jok, book)
                response = wechat.response_text(content=reply)
                return HttpResponse(response,content_type="application/xml")
            elif content.startswith('图书'): # 图书返回值为response = wechat.response_news()
                response = wechat.response_news([
                    {
                        'title': '自强学堂',
                        'picurl': 'http://www.ziqiangxuetang.com/static/images/newlogo.png',
                        'description': '自强学堂致力于提供优质的IT技术教程, 网页制作，服务器后台编写，以及编程语言，如HTML,JS,Bootstrap,Python,Django。同时也提供大量在线实例，通过实例，学习更容易，更轻松。',
                        'url': 'http://www.ziqiangxuetang.com',
                    }, {
                        'title': '百度',
                        'picurl': 'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                        'url': 'http://www.baidu.com',
                    }, {
                        'title': 'Django 教程',
                        'picurl': 'http://www.ziqiangxuetang.com/media/uploads/images/django_logo_20140508_061519_35.jpg',
                        'url': 'http://www.ziqiangxuetang.com/django/django-tutorial.html',
                    }
                ])

                # response = wechat.response_news()
                return HttpResponse(response, content_type="application/xml")
            else:
                reply = doreply(content)
                response = wechat.response_text(content=reply)
                return HttpResponse(response,content_type="application/xml")
        elif isinstance(message,VideoMessage):
            reply = '视频信息'
        elif isinstance(message,VoiceMessage):
            reply = '语音信息'
        elif isinstance(message,ShortVideoMessage):
            reply = '小视频'
        elif isinstance(message,LocationMessage):
            reply = '位置信息'
        elif isinstance(message,LinkMessage):
            reply = '链接信息'
        elif isinstance(message,ImageMessage):
            reply = '图像信息'
        elif isinstance(message,EventMessage):  # 事件信息
            if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
                reply = '您好！感谢您的关注！\n回复【功能】两字查看支持功能'

                # 如果 key 和 ticket 均不为空，则是扫描二维码造成的关注事件
                if message.key and message.ticket:
                    reply += '\n来源：扫描二维码关注'
                else:
                    reply += '\n来源：搜索名称关注'
            elif message.type == 'unsubscribe':
                reply = '取消关注事件'
            elif message.type == 'scan':
                reply = '已关注用户扫描二维码'
            elif message.type == 'location':
                reply = '上传地理位置'
            elif message.type == 'click':
                reply = '自定义菜单点击'
            elif message.type == 'view':
                reply = '自定义菜单跳转链接'
            elif message.type == 'templatesendjobfinish':
                reply = '模板消息'

        response = wechat.response_text(content=reply)
        return HttpResponse(response,content_type="application/xml")