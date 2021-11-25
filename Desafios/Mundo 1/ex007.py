print('\033[31m-=-' * 9)
print('\033[35mCalculador de Média')
print('\033[31m-=-' * 9)
n1 = float(input('\033[94mPrimeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print('\033[94mA média entre \033[1m{:.1f}\033[22m e \033[1m{:.1f}\033[22m é igual a \033[1m{:.1f}\033[22m.'
      .format(n1, n2, (n1 + n2) / 2))
