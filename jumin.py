# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
http://txt2re.com/
'''
import re

try:
    p=re.compile('\d{6}-\d{7}')
    txt="870019-1234567" #자릿수 부족으로 에러 발생 try~exception적용
    m=p.search(txt)  #check if there is a match
    print(m.group())
    print()

except:
    print("Jumin number is incorrect")
    print("Please input the number in the correct formation(6-7)")
    
print("Jumin number:", txt)
print("Max parking hours: 3 hrs")
print("Receipt required")