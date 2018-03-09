# -*- coding: utf-8 -*-
'''
Created on 2017. 11. 26.

@author: Heok Joon Son
'''
import copy

my = {}  #Dictionary type
fileName="D:\\TestBank\\calendar.txt"
bl = True
num=0


while bl:
    print()
    print("1.등록   2.전체출력   3.종료")
    num=int(input(">>> "))
    if num==1:
        outfile = open(fileName, "a", encoding="utf-8")
        number=input("날짜?")
        dt = number + " "
        a=input("오전시간:할일 등록?")  #7:wake up
        dt = dt + a + " "
        b=input("오후시간:할일 등록?")  #8:breakfast
        dt = dt + b + "\n"
        print(dt)
        outfile.write(dt)
        outfile.close()
    elif num==2:
        rfile = open(fileName, "r", encoding="utf-8")
        print(rfile.read())
        rfile.close()
    elif num==3:
        print("\n프로그램을 종료합니다.")
        bl = False


        