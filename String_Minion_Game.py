# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:13:59 2019

@author: sanjain6
"""

#Kevin and Stuart want to play the 'The Minion Game'.
#
#Game Rules
#
#Both players are given the same string, .
#Both players have to make substrings using the letters of the string .
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.
#
#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.

#Your task is to determine the winner of the game and their score.
#
#Input Format
#
#A single line of input containing the string .
#Note: The string  will contain only uppercase letters: .
#
#Constraints
#
#
#
#Output Format
#
#Print one line: the name of the winner and their score separated by a space.
#
#If the game is a draw, print Draw.
#
#Sample Input
#
#BANANA
#Sample Output
#
#Stuart 12


def minion_game(string):
    # your code goes here
    vowel = "AEIOU"
    countk= 0 
    counts =0
    for i in range(len(string)):
        if s[i] in vowel:
            countk+= len(s) - i
        else:
            counts+= len(s) - i

    if countk > counts:
        print("Kevin ",countk, end="")
    elif countk < counts:
        print("Stuart ",counts, end="")
    else:
        print("Draw", end="")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)















