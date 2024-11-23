employees_name = str(input())
salary = float(input())
sold = float(input())

bonus = (sold*0.15) + salary

print(f'TOTAL = R$ {bonus:.2f}')