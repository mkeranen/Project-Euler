# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:49:43 2017

@author: mkeranen

Project Euler - Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000 (non-inclusive).
"""
#Initialize list from 0 to 1000 (non-inclusive)
numList = [i for i in range(0,1000)]
listToSum = []

#Check if multiple of 3 or 5, if yes, append to new list
for num in numList:
    if num % 3 == 0 or num % 5 == 0:
        listToSum.append(num)
        
#Sum the list of multiples and report the result
print('Sum of muliples of 3 or 5 below 1000 is: {}'.format(sum(listToSum)))