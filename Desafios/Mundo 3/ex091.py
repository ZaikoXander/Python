"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário em Python.
    No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

print('Temos 4 jogadores...')
sleep(0.5)
print('Eles jogam seus dados para saberem o ranking!')
sleep(1)
print('Eeee...\n')
sleep(0.5)

jogadores = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}

print('Valores sorteados:')
sleep(1)

for k, v in jogadores.items():
    print(f'   O {k} tirou {v}')
    sleep(0.5)

print('Ranking dos jogadores:')
sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(ranking):
    print(f'   O {k + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
