#!/usr/bin/env python3
import requests, sys
from urllib import request
import _thread, os


def dd(d=''):
    print(d)
    sys.exit("[执行中断]")


def main(param, page):
    post_url = "https://api.chuangkit.com/designtemplate/getAllTemplates.do?_dataType=json"
    post_response = requests.post(url=post_url, data=param)
    post_data = post_response.json()
    body_list = post_data['body']['queryDesignTemplateBeanList']
    for bl in body_list:
        img_url = bl['designTemplateImageUrl']
        img_url = img_url.lstrip('//')
        title = bl['templateTitle']
        n_url = 'https://' + img_url + '?&x-oss-process=image/sharpen,100'
        print(n_url)
        status = requests.get(n_url).status_code
        print(status)
        if status != 200:
            sys.exit()
        file_path = 'wx_headimg/第%s页/' % (page)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        request.urlretrieve(n_url, file_path + title + '.jpg')
        print(title + "--------》下载完成")

if __name__ == '__main__':
    i = 1
    while True:
        param = {
            'pageNo': i,
            'pageSize': '',
            'parentKindId': 4,
            'secondKindId': 213,
            'timeOrder': 0,
            'useTimesOrder': 0,
            'collectionTimesOrder': 0,
            'stickOrder': 1,
            #    priceType:
            #    usage:
            #    time:
            'copyright': 0,
            #   id:
            #   content_price_type_filter:
            #   accurate_search: 1
            'effect_search': 1,
            '_dataClientType': 0,
            'client_type': 0
        }
        print(param)
        res = main(param, i)
        i+=1
        print(i)
