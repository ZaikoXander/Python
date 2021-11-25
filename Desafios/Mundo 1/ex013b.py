from time import sleep
preco = float(input('\033[1;95;40mDigite o valor do produto: \033[93mR$'))
print('\033[97mObs.: O pagamento à vista contém um desconto de 20%.\033[49m\n')
sleep(2)
print('\033[94;40mO produto de valor \033[93mR${:.2f}\033[94m sendo pago à vista sai pelo valor de '
      '\033[93mR${:.2f}\033[94m!\033[m'.format(preco, preco * 0.80))
