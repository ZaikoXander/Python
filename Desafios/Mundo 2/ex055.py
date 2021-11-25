print('\033[1;93mDigite o peso de 5 pessoas diferentes:')
menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('\033[97mPeso da {}ª pessoa: (kg)'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[92mO maior peso foi {}kg e o menor foi {}kg!'.format(maior, menor))
