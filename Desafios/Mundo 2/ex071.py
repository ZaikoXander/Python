print('\033[1;97m-' * 16)
print('| \033[91mBanco Xandêncio \033[97m|')
print('-' * 16)
while True:
    valor = input('\033[97mQue valor você quer sacar? \033[93mR$')
    if valor.isnumeric():
        valor = int(valor)
        break
total = valor
cedula = 50
cont = 0
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print('\033[97mTotal de \033[91m{} \033[97mcédulas de \033[93mR${}'.format(cont, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break
print('\n\033[97mVolte sempre ao \033[91mBanco Xander\033[97m! Tenha um bom dia!')
