"""
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
    Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

pessoa = {'nome': str(input('Nome: ')),
          'idade': date.today().year - int(input('Ano de nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 não tem): '))}

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa.update({'salário': float(input('Salário: ')),
                   'aposentadoria': (pessoa['contratação'] + 35) - (date.today().year - pessoa['idade'])})
                   
print('-=' * 20 + '-\n'
      f'{pessoa}')

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
