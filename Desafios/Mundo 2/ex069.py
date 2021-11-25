maiores = homens = mulher20 = 0
while True:
    print('\033[1;97m-' * 23)
    print('| \033[91mCadastre uma pessoa \033[97m|'.format('Cadastre uma pessoa'))
    print('-' * 23)
    # while True:
    #     idade = input('Idade: ').strip()
    #     if idade.isnumeric():
    #         idade = int(idade)
    #         break
    idade = ''
    while not idade.isnumeric():
        idade = input('Idade: ').strip()
    idade = int(idade)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [\033[91mM\033[97m/\033[91mF\033[97m] ')).strip().upper()[0]
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [\033[91mS\033[97m/\033[91mN\033[97m] ')).strip().upper()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulher20 += 1
    if opcao == 'N':
        break
print('\nTotal de pessoas com mais de 18 anos: {}'.format(maiores))
if homens == 0:
    print('Ao todo temos nenhum homem cadastrado.')
elif homens == 1:
    print('Ao todo temos 1 homem cadastrado.')
else:
    print('Ao todo temos {} homens cadastrados.'.format(homens))
if mulher20 == 0:
    print('E temos nenhuma mulher com menos de 20 anos.')
elif mulher20 == 1:
    print('E temos 1 mulher com menos de 20 anos.')
else:
    print('E temos {} mulheres com menos de 20 anos.'.format(mulher20))
