"""
    Aprimore o desafio 93 para que ele funcione com vários jogadores,
    incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

time = []
jogador = {}
while True:
    jogador.clear()
    jogador = {'nome': str(input('Nome do Jogador: ')), 'gols': []}
    totpart = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for p in range(0, totpart):
        jogador['gols'].append(int(input(f'Quantos gols na partida {p + 1}? ')))

    jogador['total'] = 0
    for gols in jogador['gols']:
        jogador['total'] += gols

    time.append(jogador.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N por favor.')

    if resp == 'N':
        break

print('-=' * 20 + '-')
print(f'{"cod":<5}{"nome"}{"gols":>15}{"total":>15}')
print('-' * 40)

for k, v in enumerate(time):
    print(f'  {k:<5}', end='')
    for d in v.values():
        print(f'{str(d)}')
