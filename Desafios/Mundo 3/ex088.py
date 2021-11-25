from random import randint
from time import sleep
mega = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, jogos):
    mega.append([])
for i in range(0, jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in mega[i]:
            mega[i].append(num)
            cont += 1
        if cont == 6:
            break
print(f'{"-=" * 3}  SORTEANDO {jogos} JOGOS  {"=-" * 3}')
for i in range(0, jogos):
    mega[i].sort()
    print(f'Jogo {i+1}: {mega[i]}')
    sleep(1)
print(f'{"-=" * 4} < BOA SORTE > {"=-" * 4}')
