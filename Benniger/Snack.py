c, q= [int(x) for x in input().strip().split(' ')]
prices=[4.0, 4.5, 5.0, 2.0, 1.5]

sub = q*prices[c-1]
print(f'Total: R$ {sub:.2f}')