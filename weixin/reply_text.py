#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from .youdao import YouDao
from .chengyu import chengyu_dict

__author__ = 'panguosheng'


def doreply(content):
    reply = None
    try:
        if content.startswith('翻译'):
            trans_text = content[2:].encode('utf-8')
            translation = YouDao()
            reply = '%s' % (translation.trans(trans_text))
            return reply
        elif content.startswith('成语'):
            word = content[2:].encode('utf-8')
            reply = '%s' % (chengyu_dict(word))
            return reply
        else:
            pass
    except Exception as e:
        print('error:',e)

    return reply

if __name__ == '__main__':

    print(doreply('翻译天气'))