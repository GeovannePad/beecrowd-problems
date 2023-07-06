#!/usr/bin/env python

N = int(input())

hours = N // 3600
N = N - (hours * 3600)
minutes = N // 60
N = N - (minutes * 60)
seconds = N

print(f"{hours}:{minutes}:{seconds}")
