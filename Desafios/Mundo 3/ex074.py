from random import randint

numeros = (randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999))

print('Os números sorteados foram: ', end='')
for num in numeros:
    print(f'| {num} ', end='')
print('|', end='\n')

print(f'O menor valor é {min(numeros)} e o maior é {max(numeros)}')
