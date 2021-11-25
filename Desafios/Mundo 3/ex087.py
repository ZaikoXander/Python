matriz = [[], [], []]
pares = tercoluna = maiorseglinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        if num % 2 == 0:
            pares += num
        if c == 2:
            tercoluna += num
        if l == 2:
            maiorseglinha = max(matriz[l - 1])
        matriz[l].append(num)
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'\n-> A soma dos valores pares é {pares}')
print(f'-> A soma dos valores da terceira coluna é {tercoluna}')
print(f'-> O maior valor da segunda linha é {maiorseglinha}')
