
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains as ac

import requests
from bs4 import BeautifulSoup

from time import sleep
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

###### 브라우저 옵션 설정 ######

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)

#############################





# 페이지 스크롤하기
def page_scroll():
    # 지정한 위치로 스크롤 내리기
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 1080 위치로 스크롤하기
    sleep(0.1)
    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script('return document.body.scrollHeight')
    i = 0
    # 반복 수행
    while i < 5:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 1080 위치로 스크롤하기
        sleep(0.1)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script('return document.body.scrollHeight')
        if curr_height == prev_height:
            break
        prev_height = curr_height
        i += 1




# 웹페이지 해당 주소 이동

# url = "https://www.khan.co.kr/politics/president/articles" # president
# url = "https://www.khan.co.kr/politics/assembly/articles" # assembly
# url = "https://www.khan.co.kr/politics/defense-diplomacy/articles" # defense-diplomacy
# url = "https://www.khan.co.kr/politics/north-korea/articles" # north-korea
# url = "https://www.khan.co.kr/politics/election/articles" # election
url = "https://ottogi.co.kr/product/product_list.asp#!" # politics-general

browser.get(url)
# browser.maximize_window()

page_scroll()


dic_news_list = []
titlelist = []
linklist = []
image_list = []
category_list = []
# 기사 1002개 수집
number = 1002
range_num = number // 10 + 1


for page in range(1, range_num):
    
    # # 스크롤하기
    # browser.execute_script('window.scrollTo(0, 500)')

    # # 창이 뜰 때까지 대기
    # try:
    #     element = WebDriverWait(browser, 30).until(
    #         ec.presence_of_element_located((By.CLASS_NAME, "pagination"))
    #     ) 
    # finally:
    #     pass
    sleep(0.1)
    


    # # 검색창에 입력
    # send_str = input_gu + ' ' + input_sort
    # elem.send_keys(send_str)
    # elem.send_keys(Keys.ENTER)



    # 크롤링
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # 검색 방법
    # soup.find_all('div')
    # soup.find_all("div", "corp_area")
    # soup.find_all('div', {'id': 'account'})
    # text만 추출 .text

    # 태그 형식 리턴
    news_list_all = soup.find("div", "goodsList")
    # print("news_list_all",news_list_all)
    news_list = news_list_all.find_all("li", "col")
    count = len(news_list)
    print(count)

    # 데이터 수집하기
    for i in range(count):
        # 텍스트 값 얻기
        # title = news_list[i].find('h2').get_text()
        # 속성 값 얻기
        # image = news_list[i].find('a')['href']
        
        title_box = news_list[i].find('div','card-content')
        title = title_box.find('span').get_text()
        print(title)
        category = title_box.find('p').get_text()
        print(category)
        # https://ottogi.co.kr/product/product_list.asp#!
        # https://ottogi.co.kr/product/product_list.asp#none
        # https://ottogi.co.kr/product/product_view.asp?page=90&hcode=&mcode=&stxt=&orderby=BEST&idx=703
        # product_view.asp?page=90&hcode=&mcode=&stxt=&orderby=BEST&idx=703
        link = "https://ottogi.co.kr/product/"+news_list[i].find('div', 'card-reveal')['onclick'][15:-1]
        print(link)
        # https://ottogi.co.kr + /pds/product/2023-05-30_640657863[8].jpg        
        image = "https://ottogi.co.kr"+news_list[i].find('img')['src']
        print(image)
        
        print(title, link, image, category)
        
        titlelist.append(title)
        linklist.append(link)
        image_list.append(image)
        category_list.append(category)
        
    # # 필요한 뉴스 개수가 다 차면 그만
    # if len(dic_news_list) >= number:
    #     break

    
    #all > ul > li.disabled.prev > a
    #all > ul > li:nth-child(2)
    
    #all > ul > li.next
    #all > ul > li.next
    # 뉴스 다음 버튼 누르기
    try:
        eles = browser.find_element(by=By.CSS_SELECTOR, value='#all > ul > li.next')
        eles.click()
    except:
        break
    
    page += 1
    sleep(0.1)


# csv 파일로 저장하기
data = {"title" : titlelist,"link": linklist, "image": image_list, "category": category_list}
df = pd.DataFrame(data)
df.to_csv("crawling_link.csv")

print('finished saving into csv')
