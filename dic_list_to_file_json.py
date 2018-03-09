# -*- coding: utf-8 -*-
'''
Created on 2017. 11. 26.

@author: Heok Joon Son
'''
import copy
import json

my = {}  #Dictionary type
dt = []
fileName="D:\\TestBank\\calendar.txt"
bl = True
num=0
json.dump
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
        my[number]=copy.deepcopy(dt)
        dt.clear()
        file = open(fileName, "a", encoding="utf-8")
        msg=json.dumps(my)
        my.clear()
        file.writelines(msg)
        file.write("\n")
        file.close
    elif num==2:
        file = open(fileName, "r", encoding="utf-8")
        print(file.read())
        file.close()
    elif num==3:
        print("\n프로그램을 종료합니다.")
        bl = False


        