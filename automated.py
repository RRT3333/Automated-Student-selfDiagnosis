'''
automated student self-diagnosis, ASD
Copyright (c)2020 TAO
All rights reserved.
'''
# -*- coding: utf-8 -*-
# scn_Nm=scn_Nm.decode('a').encode('utf-8')
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
def jindan(n,b):
    # C:\Python\Python38/
    url = "https://eduro.goe.go.kr/stv_cvd_co00_002.do"
    driver.get(url)
    driver.find_element_by_name("frnoRidno").send_keys(b)  # 생년월일
    driver.find_element_by_name("pName").send_keys(n)  # 이름
    driver.find_element_by_name("schulNm").send_keys('돌마고등학교')  # 학교
    driver.implicitly_wait(3)
    # 확인버튼 xpath 값 가져오기
    # driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    driver.find_element_by_xpath('/html/body/app-root/div[2]/section/div/div/div/div[3]/div/button').click()
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    # driver.find_element_by_xpath('/html/body/app-root/div[2]/section/div/div/div/div[3]/div/button').click()

    driver.find_element_by_xpath('//*[@id="rspns011"]').click()  # 발열
    driver.find_element_by_xpath('//*[@id="rspns02"]').click()  # 아니오
    driver.find_element_by_xpath('//*[@id="rspns070"]').click()  # 해외여행
    driver.find_element_by_xpath('//*[@id="rspns080"]').click()  # 가족 유증상자
    driver.find_element_by_xpath('//*[@id="rspns090"]').click()  # 가족 자가격리자
    sleep(1)
    ##제출 조심!
    driver.find_element_by_xpath('/html/body/app-root/div[2]/section/div/div/div/form/div/div/button').click()   #제출
    sleep(1)
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/button').click()   #처음으로
    #driver.close()
