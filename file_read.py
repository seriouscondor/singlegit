# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
'''

file=open("D:\\TestBank\\abc.txt","r")

#a = file.read()  # return as class(that is, object)
#a = file.readline() # return as String type
a = file.readlines() # return as List type
file.close()
print(a)
