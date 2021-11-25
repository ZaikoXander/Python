from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[1;97;40mSuas opções:\033[49m
\033[92;40m[ 0 ] \033[93mPEDRA\033[49m
\033[92;40m[ 1 ] \033[93mPAPEL\033[49m
\033[92;40m[ 2 ] \033[93mTESOURA\033[49m''')
jogador = -1
while jogador < 0 or jogador > 2:
    jogador = int(input('\033[97;40mQual é a sua jogada? '))
    if jogador < 0 or jogador > 2:
        print('\033[49m\n\033[91;40mJogada inválida. Tente novamente!\033[49m\n')
print('\033[49m\n\033[40mJO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PO!!!\033[49m')
sleep(1)
print('\033[49m' + '\033[95m-~' * 12)
print('\033[94mComputador jogou \033[96m{}\033[94m!'.format(itens[computador]))
print('Jogador jogou \033[96m{}\033[94m!'.format(itens[jogador]))
print('\033[95m-~' * 12)
if computador == 0:
    if jogador == 0:
        print('\033[96mEMPATOU\033[94m!')
    elif jogador == 1:
        print('\033[94mO jogador \033[96mGANHOU\033[94m!')
    else:
        print('\033[94mO computador \033[96mGANHOU\033[94m!')
elif computador == 1:
    if jogador == 0:
        print('\033[94mO computador \033[96mGANHOU\033[94m!')
    elif jogador == 1:
        print('\033[96mEMPATOU\033[94m!')
    else:
        print('\033[94mO jogador \033[96mGANHOU\033[94m!')
else:
    if jogador == 0:
        print('\033[94mO jogador \033[96mGANHOU\033[94m!')
    elif jogador == 1:
        print('\033[94mO computador \033[96mGANHOU\033[94m!')
    else:
        print('\033[96mEMPATOU\033[94m!')
