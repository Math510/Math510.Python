# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 2+3

print(x)

y = 6

z = x + y

print(z)
print(x+y)

y = -4
if y == 1:
    print('y still equals 1, I was just checking')

if y < 1:
    print('What now?')

if y <= 1:
    print('Did this work?')
    
a = 6
if a > 5:
    print("This shouldn't happen.")
else:
    print("This should happen.")
    
if a > 5:
    print("Big number!")
elif a % 2 != 0:
    print("This is an odd number")
    print("It isn't greater than five, either")
else:
    print("this number isn't greater than 5")
    print("nor is it odd")
    print("feeling special?")
    
list = [2, 4, 6, 8]
sum = 0
for num in list:
     sum = sum + num
     print(num, sum)
print("The sum is:", sum)

a = 0
while a < 10:
    a = a + 1
    print(a)

x = 10
while x != 0:
    print(x)
    x = x - 1
    print ("wow, we've counted x down, and now it equals", x)
print ("And now the loop has ended.")