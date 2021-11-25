from math import cos, sin, tan, radians
from time import sleep
ang = float(input('\033[1;95;40mDigite o valor de um ângulo: '))
cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))
print('\033[97mCALCULANDO SENO, COSSENO E TANGENTE...\033[49m\n')
sleep(3)
print('\033[94;40mO ângulo \033[31m{:.1f}º\033[94m tem um seno de \033[31m{:.4f}\033[94m, cosseno de '
      '\033[31m{:.4f}\033[94m e tangente de \033[31m{:.4f}\033[94m!\033[49m'.format(ang, sen, cos, tan))
