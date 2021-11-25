from time import sleep
"""from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}!'.format(num, trunc(num)))"""

num = float(input('\033[1;95;40mDigite um número: '))
print('\033[97mANALISANDO NÚMERO...\033[49m\n')
sleep(3)
print('\033[94;40mO número \033[31m{}\033[94m tem a parte inteira \033[31m{}\033[94m!\033[49m'.format(num, int(num)))
