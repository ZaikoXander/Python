peso = -1
alt = -1
while peso <= 0 or peso > 210 or alt <= 0 or alt > 3:
    peso = float(input('\033[1;97;40mDigite quantos quilos você pesa: (Kg) '))
    alt = float(input('Digite qual sua altura: (m) '))
    if peso <= 0 or peso > 210 or alt <= 0 or alt > 3:
        print('\033[49m\n\033[91;40mValores inválidos. Tente novamente!\033[49m\n')
imc = peso / alt ** 2
if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc <= 25:
    status = 'Peso ideal'
elif imc <= 30:
    status = 'Sobrepeso'
elif imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print('\033[49m\n\033[94;40mSeu IMC é equivalente a {:.1f}. \033[4mStatus\033[0;1;94;40m: \033[4m{}\033[49m'
      .format(imc, status))
