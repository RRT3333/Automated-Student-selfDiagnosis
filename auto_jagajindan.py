'''
Automated Student self-Diagnosis, ASD
Copyright (c)2020 TAO mmtsd@naver.com
All rights reserved.
'''
#-* utf-8 *-
#한글 텍스트 파일 읽어오기
import automated
f=open("automated_jagajindan_stu_data.txt",'r',encoding='utf-8')
lines = f.readlines()

i=0
for line in lines:
    if(i==0 or i==1):
        i+=1
        continue
    #print(line,end='')   #txt파일의 \n도 같이 읽힘에 주의
    if(i%2==0):
        #이름
        name=line
        print(name,end='')
    else:
        #생년월일
        bit=line
        print(bit,end='')
        automated.jindan(name, bit)
    i+=1

f.close()