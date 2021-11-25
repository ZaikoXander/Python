from time import sleep
num = int(input('\033[1;95;40mDigite um número de 0 a 9999: '))
sleep(0.5)
print('\033[97mANALISANDO NÚMERO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m\n')
sleep(1)
print('\033[94;40mMilhar: {}\033[49m\n\033[40mCentena: {}\033[49m\n\033[40mDezena: {}\033[49m\n'
      '\033[40mUnidade: {}\033[49m'.format(num // 1000 % 10, num // 100 % 10, num // 10 % 10, num // 1 % 10))
