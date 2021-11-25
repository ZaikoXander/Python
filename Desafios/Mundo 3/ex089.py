from time import sleep
alunos = []
while True:
    while True:
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        m = (nota1 + nota2) / 2
        alunos.append([nome, [nota1, nota2], m])
        while True:
            opcao = input('Quer continuar? [S/N] ')
            if bool(opcao) is True and opcao[0] in 'SsNn' and opcao[0].isalpha():
                break
        if opcao[0] in 'Nn':
            break
    print('-=' * 10 + '-')
    print(f'{"No.":<4} {"Nome":<10} {"MÉDIA"}')
    print('-' * 21)
    for i in range(0, len(alunos)):
        print(f'{i:<4} {alunos[i][0]:<10} {alunos[i][2]:.1f}')
    print('-=' * 10 + '-')
    while True:
        mostrar = int(input('Mostrar notas de qual aluno? (-1 interrompe): '))
        print('-' * 40)
        if mostrar == -1:
            print(f'{"FINALIZANDO...":^20}')
            sleep(1)
            print('<<< VOLTE SEMPRE >>>')
            break
        elif mostrar < len(alunos):
            print(f'Notas de {alunos[mostrar][0]} são [{alunos[mostrar][1][0]:.1f}, {alunos[mostrar][1][1]:.1f}]')
            print('-' * 40)
        else:
            print('Tente novamente.')
    break
