from datetime import date

print('\033[1;91m-=-' * 13)
print('\033[95m|  CONFEDERAÇÃO NACIONAL DE NATAÇÃO   |')
print('\033[91m-=-' * 13)
anos = -1
while anos < 0 or anos > 140:
    nascimento = int(input('\033[97;40mDigite seu ano de nascimento: '))
    anos = date.today().year - nascimento
    if anos < 0 or anos > 140:
        print('\033[49m\n\033[91;40mData inválida, digite novamente!\033[49m')
    else:
        continue
if anos <= 9:
    atleta = 'Mirim'
elif anos <= 14:
    atleta = 'Infantil'
elif anos <= 19:
    atleta = 'Junior'
elif anos <= 25:
    atleta = 'Sênior'
else:
    atleta = 'Master'
print('\033[49m\n\033[94;40mA categoria do atleta é \033[4m{}\033[0;1;94;40m!\033[49m'.format(atleta))
