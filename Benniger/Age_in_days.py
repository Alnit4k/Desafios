d=int(input())

y = d//365
d%=365
m=d//30
d%=30

print(f'{y} ano(s)\n{m} mes(es)\n{d} dia(s)')