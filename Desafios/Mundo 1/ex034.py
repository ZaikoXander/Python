from time import sleep
salario = float(input('\033[1;95;40mQual é o salário do funcionário? \033[93mR$'))
sleep(0.5)
print('\033[97mAPLICANDO AUMENTO.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
if salario > 1250.00:
    novo = salario * 1.10
    porcentagem = '10'
else:
    novo = salario * 1.15
    porcentagem = '15'
print('\n\033[94;40mO salário antigo de valor \033[91mR${:.2f}\033[94m com um aumento de {}% começa a valer '
      '\033[92mR${:.2f}\033[94m!\033[49m'.format(salario, porcentagem, novo))
