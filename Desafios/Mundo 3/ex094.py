galera = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break

print('-=' * 30 + '-')
print(f'A) - O grupo tem {len(galera)} pessoas.')

m = 0
for p in galera:
    m+= p['idade']
m /= len(galera)

print(f'B) - A média de idade é de {m:.2f} anos.')
print('C) - As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')

print('\nD) - Lista das pessoas que estão acima da média:')

for p in galera:
    if p['idade'] > m:
        print()

        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

print('\n<<< ENCERRADO >>>')
