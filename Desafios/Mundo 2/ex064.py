num = cont = soma = 0
while num != 999:  # 999 é o flag
    num = int(input('\033[1;91mDigite um valor [999 para parar]: '))
    if num != 999:
        cont += 1
        soma += num
print('\033[97mForam digitados {} números para a parada e a soma deles é {}!'.format(cont, soma))
