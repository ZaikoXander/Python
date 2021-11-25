soma = 0
cont = 0
"""for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(s)"""
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # soma = soma + c // Acumula valores
        cont += 1  # Mais um que achei
print('A soma de todos os {} valores solicitados é {}!'.format(cont, soma))
