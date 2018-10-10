import json
import re
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


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
    response = requests.get(url, headers=headers)
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
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_page_inner(html):
    soup = BeautifulSoup(html,"html.parser")
    # title = soup.select("title")[0].get_text()
    # title1 = re.sub("：","",title)
    images_gallery = re.compile(r"gallery: JSON.parse\((.*?),", re.S)
    images = re.findall(images_gallery,html)
    print(images)


def main():
    html = get_page_url(0,"街拍")
    for url in parse_page_index(html):
        print(url)
        html = get_page_inner(url)
        parse_page_inner(html)


if __name__ == '__main__':
    main()