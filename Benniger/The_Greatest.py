import math

a= int(input())
b= int(input())
c= int(input())

form = (a+b+abs(a-b))/2
result = (form+c+abs(form-c))/2

print(f'{result:.0f} eh o maior')

