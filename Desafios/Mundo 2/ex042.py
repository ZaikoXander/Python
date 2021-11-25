print('\033[1;91m-=-' * 10)
print('\033[95m   Analisador de Triângulos')
print('\033[91m-=-' * 10)
r1 = float(input('\033[97;40mPrimeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        tipo = 'equilátero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    print('\033[49m\n\033[4;94;40mÉ possível\033[0;1;94;40m construir um triângulo {} com essas retas!\033[49m'
          .format(tipo))
else:
    print('\033[49m\n\033[4;94;40mNão é possível\033[0;1;94;40m construir um triângulo com essas retas!\033[49m')
