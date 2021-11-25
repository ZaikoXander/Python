opcao = 'S'
cont = tot = maior = menor = 0
while opcao in 'Ss':
    num = int(input('\033[1;91mDigite um valor: '))
    opcao = str(input('Quer continuar? [\033[97mS\033[91m/\033[97mN\033[91m] ')).strip()[0]
    print()
    cont += 1
    tot += num
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    if num < menor:
        menor = num
if cont == 1:
    print('\033[97mVocê digitou um único número, logo não há média, mas o único valor digitado foi {},'.format(tot))
else:
    print('\033[97mVocê digitou {} números, e a média entre os valores digitados é {:.2f},'.format(cont, tot / cont))
if maior == menor:
    print('e não há maior nem menor.')
else:
    print('o maior é {} e o menor é {}.'.format(maior, menor))
