from time import sleep
sal = float(input('\033[1;95;40mQual é o salário do funcionário? \033[93mR$'))
print('\033[97mAPLICANDO AUMENTO...\033[49m\n')
sleep(3)
print('\033[94;40mUm funcionário ganhava um salário de \033[93mR${:.2f}\033[94m e agora com \033[31m15%\033[94m de '
      'aumento recebe \033[93mR${:.2f}\033[94m!\033[m'.format(sal, sal * 1.15))
