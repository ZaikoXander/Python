from random import choice
from time import sleep
print('\033[1;93m-=-' * 9)
print('\033[94m    Sorteador de Alunos')
print('\033[93m-=-' * 9)
n1 = str(input('\033[95;40mPrimeiro aluno: ')).strip()
n2 = str(input('Segundo aluno: ')).strip()
n3 = str(input('Terceiro aluno: ')).strip()
n4 = str(input('Quarto aluno: ')).strip()
alunos = [n1, n2, n3, n4]
sleep(0.5)
print('\033[97;49m\n\033[40mAguarde.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
print('\n\033[94;40mEscolha \033[31m{}\033[94m para apagar o quadro!\033[49m'.format(choice(alunos)))
