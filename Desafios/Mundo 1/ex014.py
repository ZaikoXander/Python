c = float(input('\033[1;95;40mInforme a temperatura em \033[31mºC: '))
print('\033[94mA temperatura de \033[31m{}ºC\033[94m corresponde a \033[31m{}ºF\033[94m e também corresponde a '
      '\033[31m{}ºK\033[94m!\033[m'.format(c, c * 9 / 5 + 32, c + 273.15))
