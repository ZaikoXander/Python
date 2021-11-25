from math import hypot
from time import sleep
co = float(input('\033[1;95;40mDigite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[97mCALCULANDO HIPOTENUSA...\033[49m\n')
sleep(3)
print('\033[94;40mO triângulo retangulo de cateto oposto \033[31m{:.2f}\033[94m e cateto adjacente '
      '\033[31m{:.2f}\033[94m, tem uma hipotenusa de tamanho \033[31m{:.2f}\033[94m!\033[49m'.format(co, ca, hi))
