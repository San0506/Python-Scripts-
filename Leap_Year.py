# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:00:16 2019

@author: sanjain6
"""

def leap_year(year):
    if year%4 ==0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False 
  
year = int(input("Enter a Year to test if its a leap year or not: "))
print(leap_year(year))






#Alternate solution 

#year=int(input("Enter year to be checked:"))
#if(year%4==0 and year%100!=0 or year%400==0):
#    print("The year is a leap year!)
#else:
#    print("The year isn't a leap year!)