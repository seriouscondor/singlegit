# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
'''
#open(file, mode, buffering, encoding, errors, newline, closefd, opener)


ofile=open("D:\\TestBank\\last.txt","w")
rfile=open("D:\\TestBank\\last.txt","r")

name=input("이름?")
age=input("나이?")
addr=input("주소?")

ofile.write(name+"\n")
ofile.write(age+"\n")
ofile.write(addr+"\n")
ofile.close()

a = rfile.readlines() # return as List type

print(a)

rfile.close()
