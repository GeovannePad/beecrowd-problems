#!/usr/bin/env python

values = input()
A, B, C = values.split(" ")

area_triangle = (float(A) * float(C)) / 2
area_circle = 3.14159 * float(C) ** 2
area_trapezium = 0.5 * float(C) * (float(A) + float(B))
area_square = float(B) * float(B)
area_rectangle = float(A) * float(B)

print(f"TRIANGULO: {area_triangle:.3f}")
print(f"CIRCULO: {area_circle:.3f}")
print(f"TRAPEZIO: {area_trapezium:.3f}")
print(f"QUADRADO: {area_square:.3f}")
print(f"RETANGULO: {area_rectangle:.3f}")