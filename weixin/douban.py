#!/usr/bin/env python3
# *-* coding: utf-8 *-*

import json
from urllib.parse import urlencode
from urllib.request import quote,urlopen,Request
from urllib.error import URLError

# 访问豆瓣API获取书籍数据
BOOK_URL_BASE = r'https://api.douban.com/v2/book/search'

# [
# {"title" : "失控", "description" : "", "image" : "http://xxx", "url" : "http://xxx"},
# {"title" : "失控", "description" : "", "image" : "http://xxx", "url" : "http://xxx"},
# {"title" : "失控", "description" : "", "image" : "http://xxx", "url" : "http://xxx"},
# ]


def search_book(word):
    params = {
        # 'q': word.encode('utf-8'),
        'q': quote(word),
        # 对于使用 GET 方式的获取数据 API，可以通过 fields 参数指定返回数据中的信息项的字段，以减少返回数据中开发者并不关心的部分。
        # fields 参数的格式目前只支持逗号分隔的字段名，没有 fields 参数或 fields 参数为 all 表示不做过滤。
        'fields': 'id,title,rating,average,author,publisher,price,images,alt',
        'count': 3
    }
    params = urlencode(params)
    url = "%s?%s" % (BOOK_URL_BASE, params)
    req = Request(url)
    try:
        resp = urlopen(req)
    except URLError as e:
        if hasattr(e,'reason'):
            reply = 'We failed to reach a server'
            return reply
        elif hasattr(e,'code'):
            reply = 'The server couldn\'t fulfill the request.'
            return reply
    else:
        # everything is fine
        content = json.loads(resp.read().decode('utf-8'))
        # print(content)
        books = content['books']
        # print(books)
        book_list = []
        for i, book in enumerate(books):
            item = {}
            title = '%s\t%s分\n%s\n%s\t%s' % (book['title'], book['rating']['average'],
                                             ','.join(book['author']), book['publisher'], book['price'])
            description = ''
            if i == 1:
                picUrl = book['images']['large']
            else:
                picUrl = book['images']['small']

            url = book['alt']
            item['title'] = title
            item['description'] = description
            item['image'] = picUrl
            item['url'] = url
            book_list.append(item)

        return book_list

if __name__ == "__main__":
    print(search_book('失控'))