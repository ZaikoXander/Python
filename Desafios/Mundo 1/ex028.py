from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('\033[1;93m-=-' * 20)
print('\033[94mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[93m-=-' * 20)
jogador = 10
while jogador > 5 or jogador < 0:
    jogador = int(input('\033[95;40mEm que número eu pensei? '))  # Jogador tenta adivinhar
    if jogador > 5 or jogador < 0:
        print('\033[35mO número digitado não pode ser usado. Tente novamente!\033[49m')
sleep(0.5)
print('\033[97mPROCESSANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
if jogador == computador:
    print('\033[92;40mPARABÉNS! Você conseguiu me vencer!\033[49m')
else:
    print('\033[91;40mGANHEI! Eu pensei no número {} e não no {}!\033[49m'.format(computador, jogador))
