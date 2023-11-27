#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
x = abs(number) % 10
if x > 5:
  print('Last digit of',number, 'is', x,' and is greater than 5')
if x == 0:
  print('Last digit of',number, 'is', x,' and is 0')
if x < 6 and x !=0:
  print('Last digit of',number, 'is', x,' and is less than 6 and not 0')

