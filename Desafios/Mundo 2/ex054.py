from datetime import date
print('\033[1;96mDigite 7 anos nascimentos de pessoas diferentes:')
menor = 0
maior = 0
for pess in range(1, 8):
    nasc = int(input('\033[97mEm que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = date.today().year - nasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('\033[91mDestes anos de nascimento {} são de menores de idade!'.format(menor))
print('\033[92mE {} destes anos de nascimento são de maiores de idade!'.format(maior))
