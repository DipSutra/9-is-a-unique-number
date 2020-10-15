# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:30:02 2020

@author: Dipankar
"""
#LEADS TO "9"
x=1
while(x<200):
    n=360
    n=n/2**x
    print(n)
    a=str(n)
    s=0
    count=0
    z=str(a)
    while(len(z)!=1):
        s=0
        for i in z:
            count=count+1
            if(ord(i)>=48 and ord(i)<=57):
                s=s+int(i)
                z=str(s)
            elif(ord(i)==101):
                break
        print(s)
    if(s!=9):
        print("solved")
        print(x, s, n)
        break
    x=x+1
print("ran for",count," times")
    #return(s)        
input("press any key to exit")
"""
n=360
n=1.0728836059570312
z=str(n)   
print(n)
while(len(z)!=1):
    s=0
    for i in z:
        if(ord(i)>=48 and ord(i)<=57):
            s=s+int(i)
            z=str(s)
        elif(ord(i)==101):
            break
     
print(s)
"""
    
    
    
    