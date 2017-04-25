#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from urllib.parse import urlencode
from urllib.request import quote,urlopen,Request
from urllib.error import URLError


CHENGYU_APIKEY = '086837705d6b15df8c5fe8a6e35e8991'


def chengyu_dict(content):

    error_code = {'10001': '错误的请求KEY',
                  '10002': '该KEY无请求权限',
                  '10003': 'KEY过期',
                  '10004': '错误的OPENID',
                  '10005': '应用未审核超时，请提交认证',
                  '10007': '未知的请求源',
                  '10008': '被禁止的IP',
                  '10009': '被禁止的KEY',
                  '10011': '当前IP请求超过限制',
                  '10012': '请求超过次数限制',
                  '10013': '测试KEY超过请求限制',
                  '10014': '系统内部异常',
                  '10020': '接口维护',
                  '10021': '接口停用',}

    base_url = r'http://v.juhe.cn/chengyu/query'
    word = quote(content)

    url = '%s?key=%s&word=' % (base_url,CHENGYU_APIKEY)
    url = url + word
    req = Request(url)
    try:
        resp = urlopen(req)
    except URLError as e:
        if hasattr(e,'reason'):
            reply = 'We failed to reach a server.'
            return reply
        elif hasattr(e, 'code'):
            reply = 'The server could not fulfill the request.'
            return reply
    else:  # everything is fine
        js = json.loads(resp.read().decode('utf-8'))
        if js['error_code'] == 0:
            reply = '【拼音】%s\n' \
                    '【成语解释】%s\n' \
                    '【成语出处】%s\n' \
                    '【举例】%s\n' \
                    '【语法】%s\n' \
                    '【词语解释】%s\n' \
                    '【引证解释】%s\n' \
                    '【同义词】%s\n' \
                    '【反义词】%s\n' % (
                js['result']['pinyin'],
                js['result']['chengyujs'],
                js['result']['from_'],
                js['result']['example'],
                js['result']['yufa'],
                js['result']['ciyujs'],
                js['result']['yinzhengjs'],
                js['result']['tongyi'],
                js['result']['fanyi']
                )
            return reply

        else:
            return error_code[js['error_code']]

if __name__ == '__main__':
    print(chengyu_dict('积少成多'))