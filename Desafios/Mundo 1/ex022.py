from time import sleep
nome = str(input('\033[1;95;40mDigite seu nome inteiro: ')).strip()
sleep(0.5)
print('\033[97mANALISANDO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m\n')
sleep(1)
print('\033[94;40mEm maiúsculo: \033[31m{}\033[94m\033[49m\n\033[40mEm minúsculo: \033[31m{}\033[94m\033[49m\n'
      '\033[40mTem \033[31m{}\033[94m letras.\033[49m\n\033[40mTem \033[31m{}\033[94m letras no primeiro nome.\033[49m'
      .format(nome.upper(), nome.lower(), len(nome.replace(' ', '')), len(nome.split()[0])))
#     .format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.find(' '))
