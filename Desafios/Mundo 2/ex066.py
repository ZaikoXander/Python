cont = soma = 0
while True:
    num = int(input('\033[1;97mDigite um valor (\033[91m999 para parar\033[97m): '))
    if num == 999:
        break
    cont += 1
    soma += num
if cont == 0:
    print('\nNenhum número foi digitado.')
else:
    # print(f'Foram digitados {cont} números e a soma deles vale {soma}.')
    print('\nForam digitados \033[91m{}\033[97m números e a soma deles vale \033[91m{}\033[97m.'.format(cont, soma))
