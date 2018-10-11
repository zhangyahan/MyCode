import json
import os
import re
import time
from multiprocessing.pool import Pool
from urllib.parse import urlencode
from hashlib import md5
from config import *
from threading import Thread
import requests
from bs4 import BeautifulSoup
import datetime


def get_page_url(offset,keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab": "3",
        "from": "gallery",
    }
    headers = {"user - agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.84Safari / 537.36"}
    url = "https://www.toutiao.com/search_content/?" + urlencode(data)
    response = requests.get(url, headers=headers, timeout=9)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and "data" in data.keys():
        for item in data.get("data"):
            yield item["article_url"]


def get_page_inner(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }
    response = requests.get(url,headers=headers, timeout=9)
    if response.status_code == 200:
        return response.text
    else:
        response.raise_for_status()


def parse_page_inner(html,url):
    soup = BeautifulSoup(html,"html.parser")
    title = soup.select("title")[0].get_text()
    images_gallery = re.compile(r"gallery: JSON.parse\(\"(.*?)\"\)", re.S)
    images = re.findall(images_gallery,html)
    image = re.sub(r'\\','',images[0])
    if image:
        data = json.loads(image)
        if data and "sub_images" in data.keys():
            sub_images = data.get("sub_images")
            sub_image = [item.get("url_list") for item in sub_images]
            urls = []
            for img in sub_image:
                urls.append(img[0].get("url"))

            for i in urls: get_photo(i, title) # 获取图片地址

            dic = {
                "title": title,
                "url": url,
                "images": urls,
            }
            return dic


def get_photo(url, title):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=9)
    if response.status_code == 200:
        insert_localhost_file(response.content, title)
    else:
        response.raise_for_status()


def insert_localhost_file(content, title):
    file_path = (os.getcwd() + "/photo/" + title)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    inner = os.path.join(file_path,md5(content).hexdigest() + ".jpg")
    if not os.path.exists(inner):
        with open(inner,"wb") as f:
            print("正在存入:",inner)
            f.write(content)
    # file_path = "{0}/{1}.{2}".format(os.getcwd() + "/photo", title + md5(content).hexdigest(), "jpg")
    # if not os.path.exists(file_path):
    #     file_path_inner = os.makedirs(file_path)
    #     print("打开" + file_path_inner)
    #     with open(file_path_inner):
    #         file_path = "{0}/{1}.{2}".format(os.getcwd() + "/photo", title + md5(content).hexdigest(), "jpg")
    #         if not os.path.exists(file_path):
    #             with open(file_path, "wb") as w:
    #                 w.write(content)
    #                 w.close()


def main(page):
    html = get_page_url(page,keyword)
    if html:
        tlist = []
        try:
            for url in parse_page_index(html):
                html = get_page_inner(url)
                if html:
                    t = Thread(target=parse_page_inner,args=(html,url))
                    tlist.append(t)
                    print("开启线程",t)
                    t.start()
                    # data = parse_page_inner(html,url)
        except KeyError as k:
            print(k)
        except requests.exceptions.ConnectTimeout as reC:
            print(reC)
        finally:
            for t in tlist:
                print("关闭线程",t)
                t.join()



if __name__ == '__main__':
    statr = time.time()
    pool = Pool()
    pool.map(main,[i*20 for i in range(page_start,page_end+1)])
    end = time.time()
    print(end-statr)
