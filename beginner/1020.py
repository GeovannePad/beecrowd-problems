#!/usr/bin/env python

age = int(input())

years = age // 365
age = age - (years * 365)

months = age // 30
age = age - (months * 30)

days = age

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")