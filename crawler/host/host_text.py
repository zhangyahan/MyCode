import requests
import re
import host_text_config
import csv
from threading import Thread

class getData():
    def __init__(self,url,page,PATH):
        self.url = url
        self.page = page
        self.PATH = PATH

    # 获取第一索引页HTML
    def start(self):
        self.csv_file = open(self.PATH, 'a', newline="", encoding="UTF-8")
        for i in range(1,self.page+1):
            url = self.url + "/zufang/pg" + str(i) + "/#contentList"
            respon = requests.get(url,params=host_text_config.herad)
            if respon.status_code == 200:
                self.one_url(respon)
            else:
                print("")
        self.csv_file.close()


    # 正则出第一界面的房屋详情url
    def one_url(self,respon):
        one_url_lists = re.findall("<a.*?href=\"(.*?\.html)\">",respon.text)
        one_url_list = []
        for i in one_url_lists[::3]:
            one_url_list.append(url + i)
        self.two_html(one_url_list)


    def mycsv(self,list):
        w = csv.writer(self.csv_file)
        w.writerow(list)


    def two_html(self,list):
        for i in list:
            respon = requests.get(i,params=host_text_config.herad)
            if respon.status_code == 200:
                host_lsit = self.two_data(respon.text,i)
                self.mycsv(host_lsit)
            else:
                print("")

    # 获取房屋详情页的信息
    def two_data(self,respon,url):
        parton1 = re.compile("<p.*?content__title\">(.*?)</p>.*?<p.*?content__aside--title\"><span>"
                             "(.*?)</span>.*?</p>.*?<span>.*?<a.*?target=\"_blank\">(.*?)</a>.*?<a.*?"
                             "target=\"_blank\">(.*?)</a>"
                             "(.*?)</span>", re.S)

        parton2 = re.compile("<span>(.*?)<span>.*?</span>.*?</span>.*?<p.*?online\">(.*?)</p>"
                            ".*?<p.*?online\">(.*?)<span.*?data-houseCode=\"\">",re.S)

        host_list = []
        host_lists = re.findall(parton1,respon)
        if not host_lists:
            host_lists = re.findall(parton2, respon)
            host_list.append(host_lists[0][1].strip())
            addr = ""
            for i in host_lists[0][2:]:
                addr += i.strip()
            host_list.append(addr)
            host_list.append(host_lists[0][0].strip())
            host_list.append(url)
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
            host_list.append(url)
            return host_list


url = "https://tj.zu.ke.com"
page = 1
PATH = "./host.csv"
def main():
    for i in range(1,page):
        t = Thread(target=getData,args=(url, i, PATH,))
        t.start()



if __name__ == '__main__':
    main()