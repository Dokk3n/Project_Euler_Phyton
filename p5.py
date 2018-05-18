#!/usr/bin/python

#https://projecteuler.net/problem=5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

notzero = True
num=20
i=1
while notzero:
	while i<21:
		if num%i == 0:
			if (i == 20): notzero = False
			i+=1
		else:
			num+=1
			i=1

print 'RESULTAT: ',num