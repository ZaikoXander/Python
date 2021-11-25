from time import sleep
dias = int(input('\033[1;95;40mQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preco = dias * 60 + km * 0.15
print('\033[97mCALCULANDO PREÇO A PAGAR...\033[49m\n')
sleep(3)
print('\033[94;40mO total a pagar pelo aluguel é de \033[93mR${:.2f}\033[94m!\033[m'.format(preco))
