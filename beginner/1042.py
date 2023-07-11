#!/usr/bin/env python

numbers = list(map(int, input().split(" ")))

for number in sorted(numbers):
    print(number)
    
print()

for number in numbers:
    print(number)