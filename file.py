# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
'''

file=open("D:\\TestBank\\abc.txt","a")
name=input("이름?")
age=input("나이?")
addr=input("주소?")

file.write(name+"\n")
file.write(age+"\n")
file.write(addr+"\n")
file.close();
print("abc.txt 파일기록 성공했습니다.")