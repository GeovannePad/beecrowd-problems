#!/usr/bin/env python

numbers = list(map(float, input().split(" ")))
sorted_numbers = sorted(numbers, reverse=True)
A, B, C = sorted_numbers

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
    exit()
    
if (A ** 2) == ((B ** 2) + (C ** 2)):
    print("TRIANGULO RETANGULO")
    
if (A ** 2) > ((B ** 2) + (C ** 2)):
    print("TRIANGULO OBTUSANGULO")
    
if (A ** 2) < ((B ** 2) + (C ** 2)):
    print("TRIANGULO ACUTANGULO")
    
if A == B == C:
    print("TRIANGULO EQUILATERO")
    
if (A == B != C) or (A == C != B) or (C == B != A):
    print("TRIANGULO ISOSCELES")