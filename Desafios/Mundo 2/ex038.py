print('\033[1;91m-=-' * 9)
print('\033[95m   Comparador de Números')
print('\033[91m-=-' * 9)

num1 = int(input('\033[97;40mDigite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
if num1 > num2:
    print('\033[49m\n\033[91;40mO primeiro número de valor {} é maior.\033[49m'.format(num1))
elif num2 > num1:
    print('\033[49m\n\033[91;40mO segundo número de valor {} é maior.\033[49m'.format(num2))
else:
    print('\033[49m\n\033[91;40mNão existe valor maior, os dois digitados são iguais.\033[49m')
