lista = []
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
        lista.append(num)

        break

    while True:
        opcao = input('Quer continuar? [S/N] ')

        if opcao[0] in 'SsNn':
            break
        print('Opção inválida, tente novamente.')

    if opcao[0] in 'Nn':
        break

pares = []
impares = []
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('\n-> Lista: [ ', end='')
for v in lista:
    print(f'{v} ', end='')
print(']')

print('-> Lista de pares: [ ', end='')
for p in pares:
    print(f'{p} ', end='')
print(']')

print('-> Lista de ímpares: [ ', end='')
for i in impares:
    print(f'{i} ', end='')
print(']')
