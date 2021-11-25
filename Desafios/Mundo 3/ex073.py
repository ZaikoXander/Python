from time import sleep
times = ('Bragatino', 'Athletico-PR', 'Fortaleza', 'Palmeiras', 'Atlético-GO', 'Atlético-MG', 'Flamengo', 'Fluminense',
         'Bahia', 'Santos', 'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife', 'Cuiabá',
         'Chapecoense', 'São Paulo', 'América-MG', 'Grêmio')
alfa = sorted(times)

print('    --  Campeonato Brasileiro  --')
print('5 Primeiros Colocados')
for c in range(0, 5):
    print(f'  {c+1}# {times[c]}')
sleep(10)
print('\nÚltimos 4 Colocados')
for c in range(16, 20):
    print(f'  {c+1}# {times[c]}')
sleep(10)
print('\nTimes Em Ordem Alfabética')
i = 0
for c in range(0, 20):
    i += 1
    print(' - ', end='')
    print(alfa[c], end='')
    if i == 4:
        i = 0
        print(' -')
sleep(10)
print(f'\nO Chapecoense está na posição: {times.index("Chapecoense") + 1}#')
