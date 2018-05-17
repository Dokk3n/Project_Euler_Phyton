# https://projecteuler.net/problem=3
# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
#COPY
from math import sqrt

a = 600851475143
sqrt_a = sqrt(a)
x = 2
while x <= sqrt_a:
    if a%x == 0:
        a /= x
        sqrt_a = sqrt(a)
    else:
        x += 1
print a