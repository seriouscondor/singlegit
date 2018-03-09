# -*- coding: utf-8 -*-
'''
Created on 2017. 12. 17.

@author: Administrator
'''

readStr,outStr,saveStr="","",""
i, secu = 0, 0
suls=[ ]
choice=input("1.파일저장   2.파일불러오기  선택? ") # oh my god, big bug, I patched for you.
fileName = "D:\\TestBank\\my.txt"

if choice =='1':
    content = input(Chage here for github : ")  #장문으로 입력
    #outFile = open(fileName,'a',encoding='utf-8')
    outFile = open(fileName,'w', encoding='utf-8')
    for i in range(0,len(content)):
        if (content[i] >= 'a' and content[i] <='z') or (content[i] >= 'A' and content[i] <='Z'):
            secu = 60
        elif content[i] >= '0' and content[i] <='9':
            secu = 10
        else:
            secu = 130
        suls.append(ord(content[i]))
        suls[i]=suls[i]+secu
        ch2=chr(suls[i])
        outStr=outStr+ch2
    outFile.write(outStr) 
    outFile.close()
    print("암호화 저장 성공했습니다")
    
elif choice =='2':
    readFile=open(fileName,'r',encoding='utf-8')
    readStr = readFile.read()
    for i in range(0,len(readStr)):
        num=ord(readStr[i])
        if chr(num-10) >= '0' and chr(num-10) <='9':
            secu = 10
        elif (chr(num-60) >= 'a' and chr(num-60) <='z')  or (chr(num-60) >= 'A' and chr(num-60) <='Z'):
            secu = 60
        else:
            secu = 130
        suls.append(ord(readStr[i]))
        suls[i] = suls[i]-secu
        ch2=chr(suls[i])
        saveStr=saveStr+ch2
    print(saveStr)
    print("\n암호화 파일로드 성공했습니다")
    # ord() 함수 : 문자의 고유한 숫자를 알려줌
    # chr() 함수 : 숫자에 해당하는 문자를 알려줌
    print("\n파일에서 가져온 값 : ",saveStr);readFile.close()
    # 위의 내용을 토대로 들어오는 값에 따라 암호화 방식을 변경하시오.
    # 들어온 값이 숫자라면, +10
    # 들어온 값이 알파벳이라면, +60
    # 들어온 값이 그 외라면 +130print("\nabc.txt 파일인코딩암호화 마지막문장입니다");
    print("암호화 파일로드 성공했습니다")
