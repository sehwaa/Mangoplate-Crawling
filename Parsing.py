#Parsing.py

from Connect import *
from bs4 import BeautifulSoup

class Parsing :

    #해쉬태그 수집
    def collectHashTag(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        hashTag = []
        for dataKeyWord in soup.find_all('button'):
            if dataKeyWord.get('data-keyword') is None:
                continue
            else:
                hashTag.append(dataKeyWord.get('data-keyword'))
        return hashTag

    #해쉬태그 URL 수집
    def getLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        rlink = []
        for link in soup.find_all('a'):
            try:
                if link.get('href').find('top_lists/') != -1 :
                    if link.get('href').find('link_key') == -1 :
                        rlink.append(link.get('href'))
            except AttributeError:
                continue
        return rlink

    #맛집 URL 수집
    def getHotLink(self):
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        hotlink = []
        for link in soup.find_all('a'):
            try:
                if link.get('href').find('restaurants') != -1 :
                    if link.get('href').find('restaurant_key') == -1 :
                        hotlink.append(link.get('href'))
            except AttributeError:
                continue
        return list(set(hotlink))

    #맛집 정보 파싱, 전처리
    def parsingHot(self, url):
        connect(url)
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
            #맛집 이름
            title = soup.find("h1",{"class": "restaurant_name"})
            #맛집 평점
            rating = soup.find("strong",{"class": "rate-point"})
            #맛집 정보
            info = dict()
            info['이름'] = title.get_text()
            info['평점'] = rating.get_text().replace('\n', '')
            table = soup.find("tbody")
            for thtd in table.find_all("tr"):
                if thtd.th.get_text() != "메뉴":
                    temp = thtd.th.get_text().replace(' ', '')
                    info[temp.replace('\n', '')] = thtd.td.get_text().replace('\n', '')
                else:
                    info[thtd.th.get_text()] = thtd.td.get_text()
            return info
        except AttributeError:
            print("없음")