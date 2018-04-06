#!/usr/bin/env python2
# -*- coding: utf-8 -*-

pas = raw_input("Insert password: ")
phrase = raw_input("Insert the phrase: ")
enc_aux = ""
result = ""

for i in range(len(phrase)):
    
    if i > len(pas)-1:
       ln = (ord(phrase[i]) + (ord(pas[i%len(pas)])-97))
    
    else:
        ln = (ord(phrase[i]) + (ord(pas[i])-97))
    
    if ln > 122:
        ln = ln - 26
        
    result += chr(ln)

print result

    

