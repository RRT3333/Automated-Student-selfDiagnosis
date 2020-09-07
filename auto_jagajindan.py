'''
Automated Student self-Diagnosis, ASD2.0
Copyright (c)2020 TAO
All rights reserved.
'''
#-* utf-8 *-
#한글 텍스트 파일 읽어오기
import automated
f=open("automated_jagajindan_stu_data.txt",'r',encoding='utf-8')
lines = f.readlines()
i=0
for line in lines:
    if(i==0 or i==1 or i==2):
        i+=1
        continue
    #print(line,end='')   #txt파일의 \n도 같이 읽힘에 주의
    if(i%3==0):
        #이름
        name=line
        print(name,end='')
    elif(i%3==1):
        #생년월일
        bit=line
        print(bit,end='')
    else:
        #비밀번호
        pa=line
        #int(pa)
        print(line,end='')
        automated.jindan(name, bit, pa)
    i+=1

print("\n\ndata파일 안에 모든 학생 자가진단을 완료하였습니다.")
print("즐거운 하루 되십시오.")
f.close()