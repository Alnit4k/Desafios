import math

n1=float(input())
n2=float(input())
n3=float(input())

delta=(n2**2) - (4*n1*n3)

if delta <= 0:
    print('Impossível calcular')
else:
    r1= (-n2 + (math.sqrt(delta))) /(2*n1)
    r2= (-n2 - (math.sqrt(delta))) /(2*n1)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')