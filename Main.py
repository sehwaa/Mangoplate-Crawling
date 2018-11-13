#Main.py
#coding: utf-8

from Connect import *
from ElementControl import *
from Parsing import *
from DBConnect import *

if __name__ == "__main__" :    

    #해쉬태그 url 리스트
    collect = []

    #맛집리스트 웹 자원 활용 객체
    e = Toplist()

    #웹 페이지 파싱 객체
    p = Parsing()

    #수집한 해쉬태그 리스트
    hashTag = p.collectHashTag()

    #해쉬태그 클릭 후 URL 수집
    for i in hashTag:
        e.tagClick(i)
        e.more()
        collect.append(p.getLink())
    
    #딕셔너리 형으로 카테고리 별 URL 분류
    category = dict()
    for index in range(0, len(hashTag)):
        category[hashTag[index]] = collect[index]

    categoryInURL = dict()

    #카테고리 별 URL 속 맛집 URL 수집
    for key in category.keys():
        hotlinklist = []
        for url in category[key]:
            connectCategoryURL = CategoryURL(url)
            connectCategoryURL.more()
            hotlinklist.append(p.getHotLink())
        categoryInURL[key] = hotlinklist
    
    #맛집 정보 파싱
    for key in categoryInURL.keys():
        for urllist in categoryInURL[key]:
            for url in urllist:
                try:
                    info=p.parsingHot(url)
                    info['카테고리'] = key
                    #print(str(info))
                    if(info['주소'].find('서울시') != -1):
                        insertDB(info)
                except:
                    continue

