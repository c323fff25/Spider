# -*- encoding: utf-8 -*-
# @文件: dt_spider.py
# @说明: 堆糖壁纸下载
# @时间: 2022/01/24 21:46:40
# @作者: c323fff25
# @版本: 1.0
from proxies import abu_session
from retrying import retry
import requests


@retry(wait_random_min=1000, wait_random_max=2000)
def get_data(url, headers, payload):
    response = requests.request("GET", url, headers=headers, data=payload, proxies=abu_session())
    if response.status_code == 200:
        return response.json()
    else:
        print('重试中.....')
        raise Exception('err')


@retry(wait_random_min=1000, wait_random_max=2000)
def get_content(url, headers, payload):
    response = requests.request("GET", url, headers=headers, data=payload, proxies=abu_session())
    if response.status_code == 200:
        return response.content
    else:
        print('重试中.....')
        raise Exception('err')


def main():
    url = "https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum%2Creply_count&filter_id=%E5%A3%81%E7%BA%B8&start=24&_=1643031936945"
    payload={}
    headers = {
        'accept': 'text/plain, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'sessionid=9aa590c8-4961-46be-b02b-e7f90210a44e; js=1; Hm_lvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1643031629; _fromcat=category; Hm_lpvt_d8276dcc8bdfef6bb9d5bc9e3bcfcaf4=1643031937; sessionid=9aa590c8-4961-46be-b02b-e7f90210a44e',
        'referer': 'https://www.duitang.com/category/?cat=wallpaper',
        'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = get_data(url, headers, payload)
    data = data['data']['object_list']
    for item in data:
        path = item['photo']['path']
        id = item['id']
        sub_html = get_content(path, headers, payload)
        with open(r'C:\Users\10638\Desktop\Spider\spider_scrpit\image\%s.jpg' % id, 'wb') as f:
            f.write(sub_html)


if __name__ == '__main__':
    main()