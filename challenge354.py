#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#challenge345
import math

a = int(raw_input("A: "))
smin = a+1 #a+1 because if smin = a, in the case that a has only 1 and a as divisors it returns a, not a+1 and in other cases it does not afect
for i in range(1, int(math.sqrt(a)+1)):
    if a%i == 0:
        if i + (a/i) < smin:
            smin = i + (a/i)
            
print smin