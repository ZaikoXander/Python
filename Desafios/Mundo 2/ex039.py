from datetime import date
atual = date.today().year
print('\033[1;30m-=' + '\033[92m=' * 9 + '\033[32m=' * 2 +
      '\033[92m=' * 5 + '\033[32m=' + '\033[92m=' * 3 + '\033[30m==-')
print('\033[30m|  \033[32mALISTAMENTO MILITAR  \033[30m|')
print('\033[30m-==' + '\033[92m=' * 3 + '\033[32m=' + '\033[92m=' * 5 +
      '\033[32m=' * 2 + '\033[92m=' * 9 + '\033[30m=-')
humano = 0
while humano != 1 and humano != 2:
    print('''\033[97;40mVocê é homem ou mulher?\033[49m
\033[92;40m[ 1 ] \033[93mHomem\033[49m
\033[92;40m[ 2 ] \033[93mMulher\033[49m''')
    humano = int(input('\033[97;40mEscolha uma opção: '))
    if humano == 1:
        continue
    elif humano == 2:
        print('\033[49m\n\033[94;40mO alistamento militar não é obrigatório para mulheres!\033[49m')
        exit()
    else:
        print('Opção inválida.\033[49m\n')
nasc = int(input('\033[1;97;40mAno de nascimento: '))
idade = atual - nasc
print('\033[49m\n\033[94;40mQuem nasceu em \033[93m{}\033[94m tem \033[91m{}\033[94m anos em \033[93m{}\033[94m.'
      '\033[49m'.format(nasc, idade, atual))
if idade == 18:
    print('\033[40mVocê tem que se alistar \033[4mIMEDIATAMENTE\033[0;1;94;40m!\033[49m')
elif idade < 18:
    saldo = 18 - idade
    print('\033[40mVocê ainda não tem \033[91m18\033[94m anos, ainda faltam \033[91m{}\033[94m anos para o alistamento!'
          '\033[49m'.format(saldo))
    ano = atual + saldo
    print('\033[40mSeu alistamento será em \033[93m{}\033[94m!\033[49m'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado faz {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
