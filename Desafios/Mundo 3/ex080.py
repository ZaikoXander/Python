numeros = []

for c in range(0, 5):  # >for responsável por receber os números e colocar numa lista
    while True:
        num = input(f'Digite o {c + 1}º número: ')

        if num.isnumeric() or num[0] == '-' and num[1:].isnumeric():
            # verifica se strings que são numericas ou numericas negativas
            if num[0] == '-' and num[1:].isnumeric():
                num = num[1:]
                num = int(num)
                num *= -1
            else:
                num = int(num)

            """if c == 0:  # >if responsável por ajeitar os números na lista
                numeros.append(num)
                print('Adicionado ao final da lista...')
            elif c == 1:
                if num >= numeros[c - 1]:  # testa o numero da posição 0
                    numeros.append(num)
                    print('Adicionado ao final da lista...')
                else:
                    numeros.insert(c - 1, num)
                    print(f'Adicionado na posição {n} da lista...')
            elif c == 2:
                if num >= numeros[c - 1]:  # testa o numero da posição 0
                    numeros.append(num)
                    print('Adicionado ao final da lista...')
                elif num >= numeros[c - 2]:  # testa o numero da posição 1
                    numeros.insert(c - 1, num)
                    print(f'Adicionado na posição {n} da lista...')
                else:
                    numeros.insert(c - 2, num)
                    print(f'Adicionado na posição {n - 1} da lista...')
            elif c == 3:
                if num >= numeros[c - 1]:
                    numeros.append(num)
                    print('Adicionado ao final da lista...')
                elif num >= numeros[c - 2]:
                    numeros.insert(c - 1, num)
                    print(f'Adicionado na posição {n} da lista...')
                elif num >= numeros[c - 3]:
                    numeros.insert(c - 2, num)
                    print(f'Adicionado na posição {c - 1} da lista...')
                else:
                    numeros.insert(c - 3, num)
                    print(f'Adicionado na posição {c - 2} da lista...')
            elif c == 4:
                if num >= numeros[c - 1]:
                    numeros.append(num)
                    print('Adicionado ao final da lista...')
                elif num >= numeros[c - 2]:
                    numeros.insert(c - 1, num)
                    print(f'Adicionado na posição {c} da lista...')
                elif num >= numeros[c - 3]:
                    numeros.insert(c - 2, num)
                    print(f'Adicionado na posição {c - 1} da lista...')
                elif num >= numeros[c - 4]:
                    numeros.insert(c - 3, num)
                    print(f'Adicionado na posição {c - 2} da lista...')
                else:
                    numeros.insert(c - 4, num)
                    print(f'Adicionado na posição {c - 3} da lista...')"""
            if c == 0 or num > numeros[-1]:
                numeros.append(num)
                print('Adicionado ao final da lista...')
            else:
                pos = 0
                while pos < len(numeros):
                    if num <= numeros[pos]:
                        numeros.insert(pos, num)
                        print(f'Adicionado na posição {pos + 1} da lista...')
                        break
                    pos += 1
            break
        print('Tente novamente por favor. ', end='')

print('\n  [ ', end='')  # >for responsável por mostrar a lista
for item in numeros:
    print(f'{item} ', end='')
print(']')
