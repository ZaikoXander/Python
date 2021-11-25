valores = []
i = 0

while True:  # >while responsável por receber os números e colocar numa lista
    while True:
        i += 1
        num = input(f'Digite o {i}º número: ')

        if num.isnumeric() or num[0] == '-' and num[1:].isnumeric():
            # verifica se strings que são numericas ou numericas negativas, e possibilita numeros negativos
            if num[0] == '-' and num[1:].isnumeric():
                num = num[1:]
                num = int(num)
                num *= -1
            else:
                num = int(num)

            if num not in valores:
                valores.append(num)
                print('Valor adicionado com sucesso...')
            else:
                print('Valor duplicado! Não vou adicionar...')

                i -= 1

            break

        print('Tente novamente por favor. ', end='')
        i -= 1

    while True:
        opcao = input('Quer continuar? [S/N] ')

        if opcao[0] in 'SsNn':
            break
        print('Opção inválida, tente novamente.')

    if opcao[0] in 'Nn':
        break

print('  [ ', end='')  # >for responsável por mostrar a lista
for n in sorted(valores):
    print(f'{n} ', end='')
print(']')
