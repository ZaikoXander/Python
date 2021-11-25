from random import shuffle
from time import sleep

print('\033[1;93m-=-' * 8)
print('\033[94m   Sorteador de Ordem')
print('\033[93m-=-' * 8)
n1 = ''
n2 = ''
n3 = ''
n4 = ''
while n1.isnumeric() or n1 == '' or n2.isnumeric() or n2 == ''\
        or n3.isnumeric() or n3 == '' or n4.isnumeric() or n4 == '':
    n1 = str(input('\033[95;40mPrimeiro aluno: ')).strip()
    n2 = str(input('Segundo aluno: ')).strip()
    n3 = str(input('Terceiro aluno: ')).strip()
    n4 = str(input('Quarto aluno: ')).strip()
    if n1.isalpha() and n2.isalpha() and n3.isalpha() and n4.isalpha():
        continue
    if n1.isnumeric() or n1 == '' or n2.isnumeric() or n2 == ''\
            or n3.isnumeric() or n3 == '' or n4.isnumeric() or n4 == '':
        print('\033[97;49m\n\033[40mDIGITE OS NOMES CORRETAMENTE!\033[49m\n')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
sleep(0.5)
print('\033[97;49m\n\033[40mAguarde.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
print('\n\033[94;40mA ordem de apresentação dos trabalhos será:\033[31;49m\n\033[40m1º {}\033[49m\n'
      '\033[40m2º {}\033[49m\n\033[40m3º {}\033[49m\n\033[40m4º {}\033[49m'
      .format(alunos[0], alunos[1], alunos[2], alunos[3]))
