#!/usr/bin/python

# https://projecteuler.net/problem=2
# Problem:
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


sum = 0
value = 1
last=last2 = 0

while value < 4000000:
	last2=value
	if  (value%2 == 0):	sum+=value
	value+=last
	last = last2
	print "value: ",value
	print "last: ",last
print sum