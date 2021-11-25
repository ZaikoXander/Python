sexo = '1'
while sexo not in 'MF':
    sexo = str(input('\033[1;97mSexo [\033[94mM\033[97m/\033[95mF\033[97m]: ')).strip().upper()[0]
    if sexo == 'M':
        print('Sexo Masculino registrado com sucesso!')
    elif sexo == 'F':
        print('Sexo Feminino registrado com sucesso!')
    else:
        print('\033[91mDado inválido. Tente novamente!\n')
