pessoas = []
i = 0
while True:
    i += 1
    print(f'{i}º pessoa')
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    while True:
        opcao = input('Quer continuar? [S/N] ')
        if bool(opcao) and opcao[0] in 'SsNn' and opcao[0].isalpha():
            break
    if opcao[0] in 'Nn':
        break
maior = pessoas[1]
indicemai = []
menor = pessoas[1]
indicemen = []
for i, v in enumerate(pessoas):
    if i % 2 != 0 and i != 1:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
for i, v in enumerate(pessoas):
    if v == maior:
        indicemai.append(pessoas[i-1])
    if v == menor:
        indicemen.append(pessoas[i-1])
print('\n' + '-=' * 20 + '-')
print(f'-> Foram cadastradas {int(len(pessoas) / 2)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de', end='')
for pessoamai in indicemai:
    print(pessoamai, end=' ')
print(f'\nO menor peso foi de {menor:.1f}KG. Peso de', end='')
for pessoamen in indicemen:
    print(pessoamen, end=' ')
print('-=' * 20 + '-')
