print('\033[1;97m-' * 23)
print('| \033[91m10 TERMOS DE UMA PA \033[97m|')
print('-' * 23)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = ptermo
cont = 1
print()
while cont <= 10:
    print('\033[97m{}'.format(termo), end=' \033[91m➝ ')
    termo += razao
    cont += 1
print('ACABOU')
