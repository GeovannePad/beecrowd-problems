#!/usr/bin/env python

worker_number = int(input())
worker_worked_hours = int(input())
worker_hour_receive = float(input())
salary = worker_worked_hours * worker_hour_receive
print(f"NUMBER = {worker_number}")
print(f"SALARY = U$ {salary:.2f}")