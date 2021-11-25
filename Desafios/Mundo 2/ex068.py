from random import randint
venceu = False
cont = 0
opcao = '0'
print('\033[1;97m-' * 16)
print('| \033[91mPAR OU ÍMPAR \033[97m|')
print('-' * 16)
while True:
    num = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = num + comp
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [\033[91mP\033[97m/\033[91mI\033[97m] ')).strip().upper()[0]
    print('-' * 22)
    print('Você jogou \033[91m{} \033[97me o computador \033[91m{}\033[97m.'.format(num, comp), end=' ')
    if total % 2 == 0:
        print('Total de \033[91m{} DEU PAR\033[97m'.format(total))
        if opcao == 'P':
            venceu = True
    else:
        print('Total de \033[91m{} DEU ÍMPAR\033[97m'.format(total))
        if opcao == 'I':
            venceu = True
    print('-' * 22)
    if venceu:
        cont += 1
        print('Você \033[91mVENCEU\033[97m!')
        print('Vamos jogar novamente...')
    else:
        print('Você \033[91mPERDEU\033[97m!')
        print('\033[91mGAME OVER\033[97m! ', end='')
        if cont == 0:
            print('Você venceu nenhuma vez.')
        elif cont == 1:
            print('Você venceu {} vez.'.format(cont))
        else:
            print('Você venceu {} vezes.'.format(cont))
        break
    venceu = False
    print()
