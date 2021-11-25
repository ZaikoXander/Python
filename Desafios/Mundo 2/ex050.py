soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('\033[1;95mDigite o {}º um valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\n\033[96mA soma dos {} números PARES digitados vale {}!'.format(cont, soma))
