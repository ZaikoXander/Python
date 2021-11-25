from time import sleep

acabou = False
escolhervalores = True
print('\033[1;97m-' * 15)
print('| \033[91mCALCULADORA \033[97m|')
print('-' * 15)
while escolhervalores:
    escolhervalores = False
    n1 = float(input('\033[97mPrimeiro valor: '))
    n2 = float(input('Segundo valor: '))
    sleep(0.5)
    while not acabou and escolhervalores is False:
        print('''
[ \033[91m1 \033[97m] Somar
[ \033[91m2 \033[97m] Multiplicar
[ \033[91m3 \033[97m] Ver maior
[ \033[91m4 \033[97m] Digitar novos números
[ \033[91m5 \033[97m] Sair do programa''')
        opcao = int(input('Opção escolhida: '))
        if opcao == 1:
            print('{} \033[91m+ \033[97m{} \033[91m= \033[97m{}'.format(n1, n2, n1 + n2))
        elif opcao == 2:
            print('{} \033[91mx \033[97m{} \033[91m= \033[97m{}'.format(n1, n2, n1 * n2))
        elif opcao == 3:
            maior = n1
            menor = n2
            if n2 > maior:
                maior = n2
                menor = n1
            print('{} \033[91m> \033[97m{}'.format(maior, menor))
        elif opcao == 4:
            print()
            escolhervalores = True
        elif opcao == 5:
            acabou = True
        else:
            print('\033[91mOpção inválida. Tente novamente!\033[97m')
