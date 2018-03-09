# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
'''
#open(file, mode, buffering, encoding, errors, newline, closefd, opener)

print("1.암호저장  2.암호화열기")
num=input(">>> ")
if num=='1':
    file=open("D:\\TestBank\\my.txt","w", encoding="utf-8")
    print("암호화")
    memo=input("저장할 메시지 입력")
elif num=='2':
    file=open("D:\\TestBank\\my.txt","r", encoding="utf-8")
    readStr=file.read()
    print("파일열기")
