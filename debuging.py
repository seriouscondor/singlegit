# -*- coding: utf-8 -*-
readStr, outStr, saveStr="", "", "" 
i,secu=0,0 ;
suls=[ ] 
fileName="D:\\TestBank\\mychange code.txt"
 
print("1.write  2.read  ");
num=input(">>>")
if num=='1':
    file=open(fileName, "w", encoding='utf-8');
    memo=input("memo? ")
    for i in range(0, len(memo)):
        if (memo[i] >= 'a' and memo[i] <='z') or (memo[i] >= 'A' and memo[i] <='Z'):
            secu = 60
        elif memo[i] >= '0' and memo[i] <='9':
            secu = 10
        else:
            secu = 130
        suls.append(ord(memo[i]))
        suls[i]=suls[i]+secu;   
        ch2=chr(suls[i]);
        outStr=outStr + ch2
    #print(outStr) 
    file.write(outStr)
    file.close()
    print("my.txt save OK ") 
elif num=='2':
    file=open(fileName, "r", encoding='utf-8');
    readStr=file.read();
    for i in range(0, len(readStr)):
        su=ord(readStr[i])
        if chr(su-10) >= '0' and chr(su-10) <='9':
            secu = 10
        elif (chr(su-60) >= 'a' and chr(su-60) <='z')  or (chr(su-60) >= 'A' and chr(su-60) <='Z'):
            secu = 60
        else:
            secu = 130
        suls.append(ord(readStr[i]))
        suls[i]=suls[i]-secu
        ch2=chr(suls[i])
        saveStr=saveStr+ch2
    print(saveStr)
    #print(readStr)
    print("\n암호화파일로드 성공했습니다")
    file.close()
