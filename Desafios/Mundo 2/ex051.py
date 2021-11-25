print('\033[1;97m-' * 23)
print('| \033[91m10 TERMOS DE UMA PA \033[97m|')
print('-' * 23)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = ptermo + (10 - 1) * razao
print()
for c in range(ptermo, decimo + razao, razao):
    print('\033[97m{}'.format(c), end=' \033[91m➝ ')
print('ACABOU')
