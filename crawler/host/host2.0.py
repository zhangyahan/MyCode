import csv
import re
import time
from multiprocessing import Pool
from threading import Thread

import requests


herad = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
# 文件路径
PATH = "./host.csv"

class MyThread(Thread):
    def __init__(self,func,args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.res = self.func(*self.args)

    def get_text(self):
        try:
            return self.res
        except Exception:
            return "错"

# 主函数
def main(page):
    url = "https://tj.zu.ke.com"
    urls = url + "/zufang/pg" + str(page) + "/#contentList"
    respon = requests.get(urls, params=herad)
    if respon.status_code == 200:
        one_html_text(respon.text,url)
    else:
        print("")


# 获取第一索引页内容
def one_html_text(resp,url):
    one_url_lists = re.findall("<a.*?href=\"(.*?\.html)\">", resp)
    # 返回详情页url,30个url
    one_url_list = []
    tlst = []
    # 打开目标文件
    csv_file = open(PATH, 'a', newline="", encoding="UTF-8")
    for i in one_url_lists[::3]:
        one_url_list.append(url + i)
    for i in one_url_list:
        t = MyThread(two_htm_text,args=(i,))
        t.start()
        tlst.append(t)
    for i in tlst:
        i.join()
        # 获取解析内容
        print(i.get_text())
        w = csv.writer(csv_file)
        # 将解析内容存入目标文件
        w.writerow(i.get_text())
    # 关闭文件
    csv_file.close()



def two_htm_text(two_url):
    # 根据第一索引页返回的url,获取详情页的信息并解析内容
    respon = requests.get(two_url, params=herad)
    if respon.status_code == 200:
        # one_html_text(respon.text,two_url)
        parton1 = re.compile("<p.*?content__title\">(.*?)</p>.*?<p.*?content__aside--title\"><span>"
                             "(.*?)</span>.*?</p>.*?<span>.*?<a.*?target=\"_blank\">(.*?)</a>.*?<a.*?"
                             "target=\"_blank\">(.*?)</a>"
                             "(.*?)</span>", re.S)

        parton2 = re.compile("<span>(.*?)<span>.*?</span>.*?</span>.*?<p.*?online\">(.*?)</p>"
                             ".*?<p.*?online\">(.*?)<span.*?data-houseCode=\"\">", re.S)

        host_list = []
        host_lists = re.findall(parton1, respon.text)
        if not host_lists:
            host_lists = re.findall(parton2, respon.text)
            host_list.append(host_lists[0][1].strip())
            addr = ""
            for i in host_lists[0][2:]:
                addr += i.strip()
            host_list.append(addr)
            host_list.append(host_lists[0][0].strip())
            host_list.append(two_url)
            if "公寓" in host_list[0].split(' ')[0]:
                host_list[1] += host_list[0].split(' ')[0]
            return host_list
        else:
            host_list.append(host_lists[0][0])
            addr = ""
            for i in host_lists[0][2:]:
                addr += i.strip()
            host_list.append(addr)
            host_list.append(host_lists[0][1])
            host_list.append(two_url)
            return host_list

    else:
        print("")


if __name__ == '__main__':
    state = time.time()
    pool = Pool()
    pool.map(main,[i for i in range(1,101)])

    # for i in range(1,101):
    #     main(i)
    end = time.time()
    print(end-state)

