#!/usr/bin/env python

A, B = map(int, input().split(" "))

if B >= A:
    print("Sao Multiplos" if (B % A == 0) else "Nao sao Multiplos")
elif A >= B:
    print("Sao Multiplos" if (A % B == 0) else "Nao sao Multiplos")