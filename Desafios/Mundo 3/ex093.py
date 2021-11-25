"""
    Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida.
    No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dicio = {'nome': str(input('Nome do Jogador: ')), 'gols': []}
totpart = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))

for p in range(0, totpart):
    dicio['gols'].append(int(input(f'   Quantos gols na partida {p + 1}? ')))

print('-=' * 30 + '-')

dicio['total'] = sum(dicio['gols'])
print(dicio)

print('-=' * 30 + '-')

for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30 + '-')

print(f'O jogador {dicio["nome"]} jogou {totpart} partidas.')

for k, v in enumerate(dicio['gols']):
    print(f'    => Na partida {k + 1}, fez {v} gols.')

print(f'Foi um total de {dicio["total"]} gols.')
