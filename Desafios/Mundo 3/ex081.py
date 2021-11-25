valores = []
i = 0

while True:
    while True:
        i += 1
        num = input(f'Digite o {i}º número: ')

        if num.isnumeric() or num[0] == '-' and num[1:].isnumeric():

            if num[0] == '-' and num[1:].isnumeric():
                num = num[1:]
                num = int(num)
                num *= -1
            else:
                num = int(num)

            print('Valor adicionado com sucesso...')
            valores.append(num)

            break

    while True:
        opcao = input('Quer continuar? [S/N] ')

        if opcao[0] in 'SsNn':
            break
        print('Opção inválida, tente novamente.')

    if opcao[0] in 'Nn':
        break

print('    [ ', end='')
for n in valores:
    print(f'{n} ', end='')
print(']\n')

if len(valores) == 1:
    print('-> Foi digitado apenas 1 número.')
else:
    print(f'-> Foram digitados {len(valores)} números.')

print('-> Lista dos valores ordenados de forma decrescente: [ ', end='')
for c in sorted(valores, reverse=True):
    print(f'{c} ', end='')
print(']')

if 5 in valores:
    print('-> Na lista há o valor 5.')
else:
    print('-> Na lista não há o valor 5.')
