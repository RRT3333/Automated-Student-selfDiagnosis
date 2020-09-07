'''
automated student self-diagnosis, ASD2.0
Copyright (c)2020 TAO
All rights reserved.
'''
# -*- coding: utf-8 -*-
# scn_Nm=scn_Nm.decode('a').encode('utf-8')
#from time import sleep
#from selenium import webdriver
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome("chromedriver85.exe")	#driver의 version식별을 위해서 사용할 driver의 이름 변경
def jindan(n,b,p):
    # C:\Python\Python38/
    url = "https://hcs.eduro.go.kr/"
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div[1]/section[2]/button[1]').click()
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td/button').click()
    #교육청 - 경기도
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[10]').click()
    #학교급 - 고등학교
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click()
    #학교검색
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys("ㅇㅇ고등학교")
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click()
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').send_keys(n)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(b)
    sleep(2)
    #PASSWORD
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/div[2]/div/div/div[1]/table/tbody/tr/td/input').send_keys(p)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    sleep(1)
    #SELECT_STUDENT
    driver.find_element_by_xpath('//*[@id="container"]/div[2]/section[2]/div[2]/ul/li/a/button').click()
    #SELFCK
    sleep(1)
    driver.find_element_by_css_selector('#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child(1) > dd > ul > li:nth-child(1) > label').click()   #37.5미만
    driver.find_element_by_css_selector('#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child(2) > dd > ul > li:nth-child(1) > label').click()   #기저질환 아니오
    driver.find_element_by_css_selector('#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child(3) > dd > ul > li:nth-child(1) > label').click()   #해외여행 아니오
    driver.find_element_by_css_selector('#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child(4) > dd > ul > li:nth-child(1) > label').click()   #동거가족 해외여행 아니오
    driver.find_element_by_css_selector('#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child(5) > dd > ul > li:nth-child(1) > label').click()   #동거가족 자가격리 아니오
    sleep(1)
    driver.find_element_by_css_selector('#btnConfirm').click()
    sleep(1)
    #RELOAD
    driver.find_element_by_css_selector('#topMenuBtn').click()
    driver.find_element_by_css_selector('#topMenuWrap > li:nth-child(2) > a').click()
    #tackle ALERT
    alert = driver.switch_to.alert
    alert.accept()
    sleep(1)
    #TO_LOGIN_OTHER_ACCOUNT
    driver.find_element_by_css_selector('body > app-root > div > div.secondary_pw > div > button').click()
    alert.accept()
    sleep(2)

