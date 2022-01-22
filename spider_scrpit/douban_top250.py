# -*- encoding: utf-8 -*-
# @文件: douban_top250.py
# @说明: 
# @时间: 2022/01/22 14:37:32
# @作者: c323fff25
# @版本: 1.0

import requests

from retrying import retry
from lxml import etree

@retry(wait_random_min=1000, wait_random_max=2000)
def get_data(url, headers):
    response = requests.get(url=url, headers=headers, proxies=None)
    # response.encoding = response.apparent_encoding
    if response.status_code == 200:
        return response.text
    else:
        raise Exception()


def parser_list(html):
    cons = etree.HTML(html)
    href = cons.xpath('//div[@class="hd"]/a/@href')
    for item in href:
        yield item


def parser_sub(html):
    cons = etree.HTML(html)
    video_name = cons.xpath('//h1/span[1]/text()')[0]
    video_slogan = cons.xpath('///meta[@property="og:description"]/@content')[0]
    screenwriter = ','.join(cons.xpath('//meta[@property="video:actor"]/@content'))
    print(f'电影名称:{video_name}\n电影简介:{video_slogan}\n主演:{screenwriter}')
    


def main():
    url = 'https://movie.douban.com/top250?start=0&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    html_ = get_data(url=url, headers=headers)
    for href in parser_list(html_):
        print(href)
        sub_html_ = get_data(url=href, headers=headers)
        parser_sub(sub_html_)
        


if __name__ == '__main__':
    main()