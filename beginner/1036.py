#!/usr/bin/env python

A, B, C = map(float, input().split(" "))

delta = (B ** 2) - (4 * A * C)

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    x1 = (-B + (delta ** (1/2))) / (2 * A)
    x2 = (-B - (delta ** (1/2))) / (2 * A)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
    