somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('\033[1;93m----- {}ª pessoa -----'.format(p))
    nome = str(input('\033[97mNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [\033[94mM\033[97m/\033[95mF\033[97m]: ')).strip()
    somaidade += idade
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('\033[41mA média de idade do grupo é de {} anos.\033[49m'.format(mediaidade))
print('\033[41mO homem mais velho tem {} anos e se chama {}.\033[49m'.format(maioridadehomem, nomevelho))
if totmulher20 > 1:
    print('\033[41mAo todo são {} mulheres com menos de 20 anos.\033[49m'.format(totmulher20))
elif totmulher20 == 1:
    print('\033[41mAo todo temos 1 mulher com menos de 20 anos.\033[49m')
else:
    print('\033[41mNão há mulheres com menos de 20 anos.\033[49m')
