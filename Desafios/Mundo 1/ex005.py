n = int(input('\033[1;30;107mDigite um valor:\033[m '))
print('\n\033[1;30;107mAnalisando o valor {}, seu antecessor é \033[31m{}\033[30m e seu sucessor é \033[92m{}\033[30m!'
      .format(n, n - 1, n + 1))
