#!/usr/bin/env python

worker_name = input()
worker_fixed_salary = float(input())
worker_total_sale = float(input())
worker_final_salary = worker_fixed_salary + (worker_total_sale * 0.15)
print(f"TOTAL = R$ {worker_final_salary:.2f}")