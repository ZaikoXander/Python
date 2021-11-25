palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for item in palavras:
    print(f'Na palavra {item} temos as vogais: ', end='')
    print('[', item.count('A') * 'A ' + item.count('E') * 'E ' + item.count('I') * 'I ' +
          item.count('O') * 'O ' + item.count('U') * 'U ' + ']')
