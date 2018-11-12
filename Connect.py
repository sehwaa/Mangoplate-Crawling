#Connect.py

from selenium import webdriver

#ChromeDriver로 접속, 자원 로딩시간 3초
driver = webdriver.Chrome('C:/Users/Playdata/Desktop/SETUP/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)

#웹페이지 불러오기
def initpage():
    driver.get('https://www.mangoplate.com/top_lists')

def connect(url):
    driver.get('https://www.mangoplate.com/' + url)