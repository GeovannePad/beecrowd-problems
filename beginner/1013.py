#!/usr/bin/env python

values = input()
A, B, C = values.split(" ")

maior_AB = int((int(A) + int(B) + abs(int(A) - int(B))) / 2)

maior_AB_C = int((int(maior_AB) + int(C) + abs(int(maior_AB) - int(C))) / 2)

print(f"{maior_AB_C} eh o maior")