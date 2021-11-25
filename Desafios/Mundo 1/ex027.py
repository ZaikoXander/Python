nome = str(input('\033[1;95;40mDigite seu nome inteiro: ')).split()
# print('Primeiro nome: {}\nÚltimo nome: {}'.format(nome[:nome.find(' ')], nome[nome.rfind(' ') + 1:]))
print('\033[94;49m\n\033[40mPrimeiro nome: \033[31m{}\033[94;49m\n\033[40mÚltimo nome: \033[31m{}\033[49m'
      .format(nome[0], nome[len(nome) - 1]))
