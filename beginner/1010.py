#!/usr/bin/env python

line1 = input().split(" ")
line2 = input().split(" ")

product1_code, product1_qtd, product1_price = line1
product2_code, product2_qtd, product2_price = line2

total = (int(product1_qtd) * float(product1_price)) + (int(product2_qtd) * float(product2_price))

print(f"VALOR A PAGAR: R$ {total:.2f}")