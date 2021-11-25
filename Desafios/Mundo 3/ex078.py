numeros = []

for n in range(0, 5):  # >for responsável por receber os números e colocar numa lista
    while True:
        num = input(f'Digite o {n + 1}º número: ')

        if num.isnumeric() or num[0] == '-' and num[1:].isnumeric():
            # verifica se strings são numericas ou numericas negativas
            if num[0] == '-' and num[1:].isnumeric():
                num = num[1:]
                num = int(num)
                num *= -1
            else:
                num = int(num)

            numeros.append(num)

            break

        print('Tente novamente por favor. ', end='')

print('\n[ ', end='')  # >for responsável por mostrar a lista
for n in numeros:
    print(f'{n} ', end='')
print(']')

cmax = cmin = 0  # >for responsável por identificar quantas vezes o maior e menor número apareceram
for i, v in enumerate(numeros):
    if v == max(numeros):
        cmax += 1
    if v == min(numeros):
        cmin += 1

if cmax == 1:
    print(f'O maior número listado é {max(numeros)} na posição {numeros.index(max(numeros)) + 1}', end='')
else:
    print(f'O maior número listado é {max(numeros)} nas posições ', end='')
    for i, v in enumerate(numeros):
        if v == max(numeros):
            print(f'{i + 1}.. ', end='')

if cmin == 1:
    print(f'\nO menor número listado é {min(numeros)} na posição {numeros.index(min(numeros)) + 1}')
else:
    print(f'\nO menor número listado é {min(numeros)} nas posições ', end='')
    for i, v in enumerate(numeros):
        if v == min(numeros):
            print(f'{i + 1}.. ', end='')
