n1, n2, n3, n4=[float(x) for x in input().strip().split(' ')]
average=(n1+n2+n3+n4)/4
print(f'Media: {average:.1f}')
if average >= 7 :
    print('Aluno aprovado.')
if average < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em Exame.')
    exam = float(input().strip())
    print(f'Nota do exame: {exam:.1f}')
    average = (average+exam)/2
    if average>= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print(f'Media final: {average:.1f}')
