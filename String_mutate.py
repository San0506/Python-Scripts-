# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:46:19 2019

@author: sanjain6
"""


if __name__ == '__main__':
    s = "abcab"
    c = 'abc'
    p = len(s)
    q = 0 
    for i in range(len(s) - len(c) + 1):
        if c in s[i: i + len(c)]:
            q +=1
    
    
    print(q)
        
                
    