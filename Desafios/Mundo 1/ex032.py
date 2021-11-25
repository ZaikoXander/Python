from datetime import date
from time import sleep
cores = {'fundobranco': '\033[107m',
         'negrito': '\033[1m',
         'limpatb': '\033[39;49m',
         'preto': '\033[30m',
         'vermelhoclaro': '\033[91m',
         'verdeclaro': '\033[92m'}
ano = int(input('\033[1;95;107mQue ano quer analisar? Coloque 0 para analisar o ano atual: '))
sleep(0.5)
print('\033[30mAnalisando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\n\033[94;107mO ano {} é BISSEXTO!\033[49m'.format(ano))
else:
    print('\n\033[94;107mO ano {} NÃO é BISSEXTO!\033[49m'.format(ano))
