n = float(input())

if n < 0 or n > 100:
    print('Fora de intervalo')
if n <= 25 and n > 0:
    print('Intervalo [0,25]')
if n <= 50 and n > 25:
    print('Intervalo (25,50]')
if n <= 75 and n > 50:
    print('Intervalo (50,75]')
if n <= 100 and n > 75:
    print('Intervalo (75,100]') 