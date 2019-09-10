# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:25:41 2019

@author: sanjain6
"""

#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    # write your code here
    new_line = line.split()
    line2 = "-".join(new_line)
    return line2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    