# -*- coding: utf-8 -*-

'''
Created on 2017. 11. 26.

@author: Heok Joon Son
'''
import copy


my = {}  #Dictionary
info2={}
bl = True
num=0
number=0
name=""
addr=""

while bl:
    print()
    print("1.등록   1.2 new menu 2.학번검색   3.수정   4.삭제   5.전체출력   6.종료")
    num=int(input(">>> "))
    if num==1:
        #print("등록")
        number=int(input("학번?"))
        name=input("이름?")
        addr=input("주소?")
        info2["stu#"]=number
        info2["name"]=name
        info2["addr"]=addr
        my[number]=copy.deepcopy(info2)
        info2.clear()
        print(number, "등록성공")
    elif num==2:
        #print("학번검색")
        number=int(input("검색학번 입력?"))
        if my.get(number):
            print(my.get(number))
        else:
            print(number, "학번이 없습니다.")
    elif num==3:
        number=int(input("수정할 학번 입력? "))
        if my.get(number):
            print(my.get(number))
            val=input("수정할필드항목 입력?")
            if val != '학번':
                new_val=input("수정 데이타 값?")
                my[number][val]=new_val
                print(val, "항목 수정에 성공했습니다.")
            else:
                print("학번은 수정할 수 없습니다.")
        else:
            print("해당 학번이 없습니다.")    
    elif num==4:
        #print("삭제")
        number=int("삭제할 학번 입력? ")
        if my.get(number):
            print(my.pop(number), "삭제했습니다.")
        else:
            print("해당 학번이 없습니다.")
    
    elif num==5:
        #print("전체출력")
        for item in my.items():
            print(item)  #printed as a tuple style
    
    elif num==6:
        print("\n프로그램을 종료합니다.")
        bl = False


        