#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from urllib.request import urlopen, quote, Request
from urllib.error import URLError

__author__ = 'panguosheng'

YOUDAO_KEY_FROM = 'xiaopanvlife'
YOUDAO_KEY = '960921132'
YOUDAO_DOC_TYPE = 'json'


class YouDao:
    def trans(self, word):
        base_url = r'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='
        qword = quote(word)
        url = base_url % (YOUDAO_KEY_FROM, YOUDAO_KEY, YOUDAO_DOC_TYPE)
        url = url + qword
        req = Request(url)
        try:
            resp = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                reply = 'We failed to reach a server.'
                return reply
            elif hasattr(e, 'code'):
                reply = 'The server could not fulfill the request.'
                return reply
        else:  # everything is fine
            fanyi = json.loads(resp.read().decode('utf-8'))
            if fanyi['errorCode'] == 0:
                if 'basic' in fanyi.keys():
                    trans = u'%s: %s\n【基本释义】%s\n【英式发音】%s\n【英式发音】%s\n【网络释义】\n%s' \
                            % (fanyi['query'], ''.join(fanyi['translation']),
                               ' '.join(fanyi['basic']['explains']), ' '.join(fanyi['basic']['uk-phonetic']),
                               ' '.join(fanyi['basic']['us-phonetic']), ' '.join(fanyi['web'][0]['value']))
                    return trans
                else:
                    trans = u'%s:\n【基本释义】\n%s' % (fanyi['query'], ''.join(fanyi['translation']))
                    return trans
            elif fanyi['errorCode'] == 20:
                return u'Sorry,要翻译的文本过长/::~'
            elif fanyi['errorCode'] == 30:
                return u'Sorry,无法进行有效的翻译/::~'
            elif fanyi['errorCode'] == 40:
                return u'Sorry,不支持的语言类型/::~'
            elif fanyi['errorCode'] == 60:
                return u'Sorry,无词典结果，仅在获取词典结果生效/::~'
            elif fanyi['errorCode'] == 50:
                return u'Sorry,无效的key/::~'
            else:
                return u'Sorry，您输入的单词【%s】有误/::~' % word


if __name__ == '__main__':
    translation = YouDao()
    print(translation.trans('谍影重重'))