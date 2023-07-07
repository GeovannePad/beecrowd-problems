#!/usr/bin/env python

product_code, quantity = map(int, input().split(" "))

products = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
}

if product_code == 1:
    total_value = products[1] * quantity
elif product_code == 2:
    total_value = products[2] * quantity
elif product_code == 3:
    total_value = products[3] * quantity
elif product_code == 4:
    total_value = products[4] * quantity
elif product_code == 5:
    total_value = products[5] * quantity
    
print(f"Total: R$ {total_value:.2f}")