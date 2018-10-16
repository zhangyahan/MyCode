import csv
import re
import time
from multiprocessing.pool import Pool

# 全局变量
from threading import Thread

import requests


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

# 网站地址
url = "https://sh.zu.ke.com"
# 请求头
herad = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
# 存储路径
PATH = "./shhost.csv"

def main():
    page = 100
    pool = Pool()

    pool.map(get_one_html,[i for i in range(1,page+1)])

    # get_two_html(one_html_text)
    # print(one_html_text)
    # print(len(one_html_text))


def get_one_html(page):
    # 获取网页信息
    urls = url + "/zufang/pg" + str(page) + "/#contentList"
    response = requests.get(urls,params=herad)
    if response.status_code == 200:
        response = re.findall("<a.*?href=\"(.*?\.html)\">", response.text)
        lst = []
        for i in response[::3]:
            t = MyThread(get_two_html,args=(i,))
            lst.append(t)
            t.start()
        num = 0
        csv_file = csv_files()
        w = csv.writer(csv_file)
        for i in lst:
            i.join()
            w.writerow(i.get_text())
            num += 1
            print(num)
        csv_file.close()

    else:
        return ""


def csv_files():
    return open(PATH, 'a', newline="", encoding="UTF-8")
    # w = csv.writer(csv_file)
    # csv_file.close()


def get_two_html(inner_url):
    response = requests.get(url + inner_url, params=herad)
    if response.status_code == 200:
        parton1 = re.compile("<p.*?content__title\">(.*?)</p>.*?<p.*?content__aside--title\"><span>"
                             "(.*?)</span>.*?</p>.*?<span>.*?<a.*?target=\"_blank\">(.*?)</a>.*?<a.*?"
                             "target=\"_blank\">(.*?)</a>"
                             "(.*?)</span>", re.S)

        parton2 = re.compile("<span>(.*?)<span>.*?</span>.*?</span>.*?<p.*?online\">(.*?)</p>"
                             ".*?<p.*?online\">(.*?)<span.*?data-houseCode=\"\">", re.S)

        host_list = []
        host_lists = re.findall(parton1, response.text)
        if not host_lists:
            host_lists = re.findall(parton2, response.text)
            host_list.append(host_lists[0][1].strip())
            addr = ""
            for i in host_lists[0][2:]:
                addr += i.strip()
            host_list.append(addr)
            host_list.append(host_lists[0][0].strip())
            host_list.append(url + inner_url)
            if "公寓" in host_list[0].split(' ')[0]:
                host_list[1] += host_list[0].split(' ')[0]
            # print(host_list)
            return host_list
        else:
            host_list.append(host_lists[0][0])
            addr = ""
            for i in host_lists[0][2:]:
                addr += i.strip()
            host_list.append(addr)
            host_list.append(host_lists[0][1])
            host_list.append(url + inner_url)
            # print(host_list)
            return host_list
    else:
        print("NO")



if __name__ == '__main__':
    state = time.time()
    main()
    end = time.time()
    print(end-state)
    # 关闭文件

    
