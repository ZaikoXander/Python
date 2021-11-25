n = float(input('\033[1;30;107mDigite um valor:\033[m '))
print('\033[1;30;107mSeu dobro vale \033[37m{:.2f}\033[30m, '
      'seu triplo vale \033[31m{:.2f}\033[30m e sua raiz quadrada vale \033[92m{:.2f}\033[30m.\033[m'
      .format(n * 2, n * 3, n ** (1 / 2)))
