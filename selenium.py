#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By

import time

########################################################################################################################
########################################################################################################################
########################################################################################################################

# 날짜 입력받기
input_Month = input('몇월입니까? ex) 04 , ex) 11 ')
input_Day = input('몇일입니까? ex) 05 , ex) 12 ')

URL_GENERAL_NOTICE = 'http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333'  # 일반 공지(전체 공지)의 url
CHROMEDRIVER_PATH = 'C:/Users/sbhdm/Desktop/Smart/chromedriver.exe'  # chromedriver 의 경로 (.py와 같이 있음)
title_Array = []  # 글 제목 배열
contents_Array = []  # 글 내용 배열

options = webdriver.ChromeOptions()  # chromedriver 옵션
options.add_argument('start-maximized')  # 창 최대 크기로 실행
# options.add_argument('headless')  # 창 안뜨게 실행

driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)  # 드라이버를 로드하여 driver 변수에 담기
driver.implicitly_wait(10)  # 웹페이지 로딩 최대 10초 기다리게 하기
driver.get(URL_GENERAL_NOTICE)  # 주소로 들어가기

index = 1
flag = 0
while True:
    for j in range(0, 10):
        tbody = driver.find_element(By.XPATH, '/html/body/div/table/tbody')  # 글 10개를 모두 가져옴
        tr_Array = tbody.find_elements(By.TAG_NAME, 'tr')  # 글 10개를 한 줄씩 쪼개서 tr_Array 담음
        tr = tr_Array[j]  # i번째 글을 tr 이라고 함
        if tr.find_element(By.CLASS_NAME, 'date').text[5:] == input_Month + "." + input_Day:  # i번째 글의 날짜 == 입력 날짜
            tr.find_element(By.CLASS_NAME, 'subject').click()  # i번째 글 클릭
            title_Array.append(driver.find_element(By.XPATH, '/html/body/div/table[1]/thead/tr[1]/td').text)  # 제목 리스트 추가
            contents_Array.append(driver.find_element(By.XPATH, '/html/body/div/table[1]/tbody/tr/td').text)  # 내용 리스트 추가
            driver.back()  # 뒤로가기
            flag=1
    if flag==0:
        index +=1
        if index>10 and index%10==1:
            next_button = driver.find_element_by_css_selector('body > div > div.pagination > ul > span:nth-child(4) > a:nth-child(1) > img')
            next_button.click()
            index-=10
        else:
            button = driver.find_element_by_css_selector('body > div > div.pagination > ul > span.num > a:nth-child(%d)' %index)
            button.click()
    else:
        break
        
for title in title_Array:
    print(title)
for contents in contents_Array:
    print(contents)




    
#driver.close()  # 크롬창 닫기


# In[ ]:




