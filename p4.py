#!/usr/bin/python
# coding=utf-8

#https://projecteuler.net/problem=4
#Problem:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
#------
#A pythonic way to determine if a given value is a palindrome:
#def palindrome(n):
#	return n == n[::-1]
#------
import math

def palindrome(n):
	return str(n) == str(n)[::-1]


max = 0
for i in range (900,1000):
	for j in range (900,1000):
		if palindrome(i*j): 
			if (i*j) > max: max=i*j

print max


