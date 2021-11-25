"""noves = 0
prim3 = -1
for num in range(0, 4):
    print(f'Digite o {num+1}º número: ', end='')

    if num == 0:
        n1 = int(input())
        if n1 == 9:
            noves += 1
        elif n1 == 3:
            prim3 = num
    if num == 1:
        n2 = int(input())
        if n2 == 9:
            noves += 1
        elif n2 == 3 and prim3 == -1:
            prim3 = num
    if num == 2:
        n3 = int(input())
        if n3 == 9:
            noves += 1
        elif n3 == 3 and prim3 == -1:
            prim3 = num
    if num == 3:
        n4 = int(input())
        if n4 == 9:
            noves += 1
        elif n4 == 3 and prim3 == -1:
            prim3 = num

valores = (n1, n2, n3, n4)

print('\n   [ ', end='')
for num in valores:
    print(f'{num} ', end='')
print(']\n')

if noves == 0:
    print('-> Nesta tupla de números não apareceu nenhum Nove.')
elif noves == 1:
    print('-> Nesta tupla de números apareceu 1 Nove.')
else:
    print(f'-> Nesta tupla de números apareceu {noves} Noves.')

if prim3 == -1:
    print('-> Nenhum número três foi encontrado.')
else:
    print(f'-> O número três foi encontrado primeiramente na posição {prim3 + 1}º.')

print('-> ', end='')
for num in valores:
    if num % 2 == 0:
        pares = True
        break
    pares = False

if pares:
    print('Os números pares presentes na tupla são: [ ', end='')
    for num in valores:
        if num % 2 == 0:
            print(num , end='')
    print(']')
else:
    print('Não há números pares na tupla.')"""

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print('\n   [ ', end='')
for n in num:
    print(f'{n} ', end='')
print(']\n')

if num.count(9) == 0:
    print('-> Nenhum número Nove foi encontrado nesta Tupla.')
elif num.count(9) == 1:
    print('-> 1 número Nove foi encontrado nesta Tupla.')
else:
    print(f'-> {num.count(9)} números Nove foram encontrados nesta Tupla.')

if 3 not in num:
    print('-> Nenhum número Três foi encontrado nesta Tupla.')
else:
    print(f'-> Na {num.index(3) + 1}ª posição um número Três foi encontrado nesta Tupla.')

printado = False
pares = False

print('-> ', end='')
for n in num:
    if n % 2 == 0:
        if printado is False:
            printado = True
            print('Os números pares presentes na tupla são: [ ', end='')
        pares = True
        print(n, end=' ')
if pares is True:
    print(']')
else:
    print('Não há números pares na tupla.')
