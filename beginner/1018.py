#!/usr/bin/env python

banknote_100, banknote_50, banknote_20, banknote_10, banknote_5, banknote_2, banknote_1 = 0, 0, 0, 0, 0, 0, 0

value = int(input())
print(value)

if value >= 100:
    banknote_100 = int(value / 100)
    value = value - (banknote_100 * 100)
    
if value >= 50:
    banknote_50 = int(value / 50)
    value = value - (banknote_50 * 50)
    
if value >= 20:
    banknote_20 = int(value / 20)
    value = value - (banknote_20 * 20)
    
if value >= 10:
    banknote_10 = int(value / 10)
    value = value - (banknote_10 * 10)
    
if value >= 5:
    banknote_5 = int(value / 5)
    value = value - (banknote_5 * 5)
    
if value >= 2:
    banknote_2 = int(value / 2)
    value = value - (banknote_2 * 2)
    
if value >= 1:
    banknote_1 = int(value / 1)
    value = value - (banknote_1 * 1)
    
print(f"{banknote_100} nota(s) de R$ 100,00")
print(f"{banknote_50} nota(s) de R$ 50,00")
print(f"{banknote_20} nota(s) de R$ 20,00")
print(f"{banknote_10} nota(s) de R$ 10,00")
print(f"{banknote_5} nota(s) de R$ 5,00")
print(f"{banknote_2} nota(s) de R$ 2,00")
print(f"{banknote_1} nota(s) de R$ 1,00")