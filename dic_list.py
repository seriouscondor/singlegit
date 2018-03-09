# -*- coding: utf-8 -*-
'''
Created on 2017. 11. 26.

@author: Heok Joon Son
'''
import copy

my = {}  #Dictionary type
dt = []  #List data type
bl = True
num=0

while bl:
    print()
    print("1.등록   2.전체출력   3.종료")
    num=int(input(">>> "))
    if num==1:
        number=int(input("날짜?"))
        dt.append(number)
        a=input("오전시간:할일 등록?")
        dt.append(a)
        b=input("오후시간:할일 등록?")
        dt.append(b)
        my[dt[0]]=copy.deepcopy(dt)
    elif num==2:
        for k in my.keys():
            print(k,":",my[k])
    elif num==3:
        print("\n프로그램을 종료합니다.")
        bl = False


        