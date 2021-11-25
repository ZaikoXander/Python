from time import sleep
cores = {'fundopreto': '\033[100m',
         'fundocomum': '\033[49m',
         'azulclaro': '\033[94m',
         'cianoclaro': '\033[96m',
         'vermelho': '\033[31m',
         'amareloclaro': '\033[93m'}
dis = int(input('\033[1;95;40mQual é a distância da sua viagem? '))
sleep(0.5)
print('\033[97mANALISANDO DADOS.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
print('\n\033[94;40mVocê está prestes a começar uma viagem de \033[96m{:.1f}Km\033[94m.\033[49m'.format(dis))
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
"""preco = dis * 0.5 if dis <=200 else dis * 0.45"""  # if in line / operador ternário
print('\033[91;40mSua passagem custará \033[93mR${:.2f}\033[91m.\033[49m'.format(preco))
