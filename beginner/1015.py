#!/usr/bin/env python

line1 = input()
line2 = input()

x1, y1 = line1.split(" ")
x2, y2 = line2.split(" ")

distance = ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** (1/2)

print(f"{distance:.4f}")