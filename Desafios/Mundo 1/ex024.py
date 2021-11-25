cidade = str(input('\033[1;95;40mDigite o nome de uma cidade: ')).strip()
# print(f'O nome da cidade é de um Santo? '
#     f'{"SANTO" in cidade.split()[0].upper() or "SÃO" in cidade.split().upper() or "SANTA" in cidade.split().upper()}')
# if cidade.split()[0].upper() == 'SANTO' or cidade.split()[0].upper() == 'SÃO' or cidade.split()[0].upper() == 'SANTA':
if cidade[:5].upper() == 'SANTO' or cidade[:3].upper() == 'SÃO' or cidade[:5].upper() == 'SANTA':
    print('\033[49m\n\033[94;40mA cidade começa com nome de \033[93mSanto\033[94m!\033[49m')
else:
    print('\033[49m\n\033[94;40mA cidade não começa com o nome \033[93mSanto\033[94m!\033[49m')
