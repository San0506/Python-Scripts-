# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:10:39 2019

@author: sanjain6
"""
#Question - the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left.


#
#Sample Input
#
#ABCDCDC
#CDC
#Sample Output
#
#2

def count_substring(string, sub_string):
    count = 0 
    for i in range(len(string)- len(sub_string) + 1):
        if sub_string == string[i:i + len(sub_string)]:
            count+=1
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)