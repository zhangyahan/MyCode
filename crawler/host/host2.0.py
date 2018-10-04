import re
import time
from multiprocessing import Pool

import requests
import host_text_config


# 主函数
def main(page):
    url = "https://tj.zu.ke.com"
    urls = url + "/zufang/pg" + str(page) + "/#contentList"
    respon = requests.get(urls, params=host_text_config.herad)
    if respon.status_code == 200:
        one_html_text(respon.text,url)
    else:
        print("")


# 获取第一索引页内容
def one_html_text(resp,url):
    one_url_lists = re.findall("<a.*?href=\"(.*?\.html)\">", resp)
    # 返回详情页url,30个url
    one_url_list = []
    for i in one_url_lists[::3]:
        one_url_list.append(url + i)
    two_htm_text(one_url_list)


def two_htm_text(resp):
    # 根据第一索引页返回的url,回去详情页的信息,房屋名称,房屋地址,房屋租金,房屋url
    pass


def csv_info():
    # 存入数据
    pass


if __name__ == '__main__':
    state = time.time()
    pool = Pool()
    pool.map(main,[i for i in range(1,101)])

    # for i in range(1,101):
    #     main(i)
    end = time.time()
    print(end-state)

