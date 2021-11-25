print('\033[1;91;40m-=-\033[49m' * 8)
print('\033[95;40m|  Conversor de Bases  |\033[49m')
print('\033[91;40m-=-\033[49m' * 8)
num = int(input('\n\033[97;40mDigite um número inteiro: '))
print('\033[49m\n\033[92;40m[ 1 ]\033[97m converter para \033[93mBINÁRIO\033[49m'
      '\n\033[92;40m[ 2 ]\033[97m converter para \033[93mOCTAL\033[49m'
      '\n\033[92;40m[ 3 ]\033[97m converter para \033[93mHEXADECIMAL\033[49m')
opcao = 0
while opcao != 1 and opcao != 2 and opcao != 3:
    opcao = int(input('\033[97;40mEscolhe sua opção de conversão: '))
    if opcao == 1:
        print('\033[49m\n\033[94;40mO número {} convertido para BINÁRIO é igual a {} !\033[49m'
              .format(num, bin(num)[2:]))
    elif opcao == 2:
        print('\033[49m\n\033[94;40mO número {} convertido para OCTAL é igual a {} !\033[49m'
              .format(num, oct(num)[2:]))
    elif opcao == 3:
        print('\033[49m\n\033[94;40mO número {} convertido para HEXADECIMAL é igual a {} !\033[49m'
              .format(num, hex(num)[2:]))
    else:
        print('\033[49m\n\033[91;40mOpção inválida. Tente novamente!\033[49m')
