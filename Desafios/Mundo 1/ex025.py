nome = str(input('\033[1;95;40mDigite seu nome inteiro: ')).upper()
# print('No seu nome tem Silva? {}'.format('SILVA' in nome))
if 'SILVA' in nome:
    print('\033[49m\n\033[94;40mVocê tem Silva em seu nome.\033[49m')
else:
    print('\033[49m\n\033[94;40mVocê não tem Silva em seu nome.\033[49m')
