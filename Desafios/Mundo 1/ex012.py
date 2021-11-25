from time import sleep
item = float(input('\033[1;95;40mDigite o valor do produto: \033[93mR$'))
print('\033[97mAPLICANDO DESCONTO...\033[49m\n')
sleep(3)
print('\033[94;40mO produto que custava \033[93mR${:.2f}\033[94m, na promoção com um desconto de \033[31m5%\033[94m '
      'vai custar \033[93mR${:.2f}\033[94m!\033[m'.format(item, item * 0.95))
