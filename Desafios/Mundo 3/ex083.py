expressao = input('Digite uma expressão: ')
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
