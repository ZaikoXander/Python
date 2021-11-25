numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesséis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        numero = input('Digitem um número de 0 a 20: ')
        if numero.isdigit() and 0 <= int(numero) <= 20:
            numero = int(numero)
            break
        print('Tente novamente! ', end='')
    print(f'Número por extenso: {numeros[numero]}')
    opcao = input('Quer continuar? [S/N] ')
    if opcao in 'Nn':
        break
