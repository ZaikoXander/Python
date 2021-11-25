from random import randint

acertou = False
cont = 0
computador = randint(0, 10)
print('\033[1;93m-=-' * 14)
print(' \033[91mVou pensar em um número entre 0 e 10...')
print('\033[93m-=-' * 14)
while not acertou:
    jogador = int(input('\033[97mTente adivinhar: '))
    cont += 1
    if jogador == computador and cont == 1:
        acertou = True
        print('\033[96mParabéns! Acertou de primeira!!')
    elif jogador != computador:
        if jogador < computador:
            print('\033[94mMais... Tente novamente!\n')
        else:
            print('\033[94mMenos... Tente novamente!\n')
    else:
        acertou = True
        print('\033[96mParabéns! Você acertou, mas foi necessárias {} tentativas!'.format(cont))
