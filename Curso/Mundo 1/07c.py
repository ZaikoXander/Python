# nome = str(input('Qual é o seu nome? '))
# print(f'Prazer em te conhecer {nome:20}!')
# // mesma coisa que o acima // print(f'Prazer em te conhecer {nome:<20}!')
# print(f'Prazer em te conhecer {nome:>20}!')
# print(f'Prazer em te conhecer {nome:^20}!')
# print(f'Prazer em te conher {nome:=^20}!')
n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\no produto é {},\na divisão é {:.3f},'.format(s, m, d), end=' ')
print('a Divisão inteira é {} e a potência {}'.format(di, e))
