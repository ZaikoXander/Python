cores = {'negrito': '\033[1m',
         'fundobranco': '\033[107m',
         'limpatb': '\033[39;49m',
         'azulclaro': '\033[94m',
         'verdeclaro': '\033[92m',
         'vermelho': '\033[31m',
         'magenta': '\033[35m'}
print('\033[1;95;40mDigite 3 números.\033[49m')
a = int(input('\033[97;40mPrimeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
"""if b > maior:
    maior = b
if c > maior:
    maior = c
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c"""

print('\033[49m\n\033[94;40mO \033[92mmaior\033[94m é \033[92m{}\033[94m!\033[49m\n'
      '\033[40mE o \033[91mmenor\033[94m é \033[91m{}\033[94m!\033[49m'
      .format(maior, menor))
