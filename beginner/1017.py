#!/usr/bin/env python

trip_time = int(input())
average_speed = int(input())

distance = trip_time * average_speed
liters = distance / 12

print(f"{liters:.3f}")