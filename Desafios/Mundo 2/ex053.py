frase = str(input('\033[1;93mDigite uma frase: ')).strip().upper()
palavras = frase.replace(' ', '')
inverso = palavras[::-1]
"""for letra in range(len(palavras) - 1, -1, -1):
    inverso += palavras[letra]"""
print('\033[96mO inverso de {} é {}!'.format(palavras, inverso))
if inverso == palavras:
    print('\n\033[92mTemos um palíndromo.')
else:
    print('\n\033[91mA frase digitada não é um palíndromo.')
