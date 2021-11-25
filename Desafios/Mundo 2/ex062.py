print('\033[1;97m-' * 23)
print('| \033[91m10 TERMOS DE UMA PA \033[97m|')
print('-' * 23)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = ptermo
cont = 1
total = 0
mais = 10
while mais != 0:
    if mais > 0:
        total += mais
        print()
        while cont <= total:
            print('\033[97m{}'.format(termo), end=' \033[91m➝ ')
            termo += razao
            cont += 1
        print('PAUSA')
    else:
        print('\n\033[91mNúmero de termos inválido. Tente novamente!')
    mais = int(input('\033[97mQuantos termos você quer mostrar a mais? '))
print('\n\033[91mACABOU\nProgressão finalizada com {} termos mostrados.'.format(total))
