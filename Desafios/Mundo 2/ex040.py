print('\033[1;91m-=-' * 7)
print('\033[95m|  Média de Notas   |')
print('\033[91m-=-' * 7)
m = 11
while m > 10:
    n1 = float(input('\033[97;40mPrimeira nota: '))
    n2 = float(input('Segunda nota: '))
    m = (n1 + n2) / 2
    if m <= 10:
        continue
    print('\033[49m\n\033[91;40mDigite uma nota válida!\033[49m')
if m < 5.0:
    print('\033[49m\n\033[94;40mO aluno com média de {:.1f} foi REPROVADO.\033[49m'.format(m))
elif 5 <= m < 7:
    print('\033[49m\n\033[94;40mO aluno com média de {:.1f} ficou de RECUPERAÇÃO.\033[49m'.format(m))
else:
    print('\033[49m\n\033[94;40mO aluno com média de {:.1f} foi APROVADO.\033[49m'.format(m))
