lista = [[], []]
for i in range(0, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('-=' * 20 + '-')
print('Números pares:', sorted(lista[0]))
print('Número ímpares:', sorted(lista[1]))
print('-=' * 20 + '-')
