#ElementControl.py
from Connect import *
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

#'맛집 리스트' URL 수집시 자원 활용
class Toplist:
    def __init__(self):
        initpage()

    #더보기 버튼 클릭
    def more(self):
        while(1):
            try:
                driver.find_element_by_xpath("//a[@class='btn-more']").click()
            except ElementNotVisibleException:
                break
            except WebDriverException:
                break

    #해쉬태그 클릭
    def tagClick(self, tag):
        driver.find_element_by_xpath("//button[@data-keyword='"+tag+"']").send_keys(Keys.ENTER)

#해쉬태그 URL 속 URL 수집시 자원 활용
class CategoryURL:
    def __init__(self, url):
        connect(url)
    
    #더보기 버튼 클릭
    def more(self):
        while(1):
            try:
                driver.find_element_by_xpath("//button[@class='more_btn']").click()
            except ElementNotVisibleException:
                break
            except WebDriverException:
                break
            except AttributeError:
                break