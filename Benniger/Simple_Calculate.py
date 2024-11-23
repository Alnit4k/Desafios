product_code = str(input())
units = float(input())
price = float(input())

pay= units*price

product_code1 = int(input())
units1 = int(input())
price1 = float(input())

pay1 = units1*price1

value_to_pay= pay+pay1

print(f'VALOR A PAGAR: R$ {value_to_pay:.2f}')