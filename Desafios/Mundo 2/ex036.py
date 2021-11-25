import time
print('\033[1;91m-=-' * 9)
print('\033[95m    Empréstimo Bancário')
print('\033[91m-=-' * 9)
casa = float(input('\033[97;40mQual é o valor da casa? \033[93mR$'))
salario = float(input('\033[97mQual o salário do comprador? \033[93mR$'))
anos = int(input('\033[97mEm quantos anos irá pagar? '))
prestacao = casa / (anos * 12)
if prestacao < salario * 0.3:
    print('\033[49m\n\033[94;40mEmpréstimo de valor \033[93mR${:.2f} \033[4;94mAPROVADO\033[0;1;94;40m!'
          '\033[49m\n\033[40mA prestação mensal tem o valor de \033[93mR${:.2f}\033[94m!\033[49m'
          .format(casa, prestacao))
else:
    print('\033[49m\n\033[31;40mInfelizmente o empréstimo não foi aprovado.\033[49m')
if int(time.strftime('%H%M')) <= 1200:
    print('\n\033[92;40mTenha um bom dia!\033[49m')
elif int(time.strftime('%H%M')) in range(1201, 1760):
    print('\n\033[92;40mTenha uma boa tarde!\033[49m')
else:
    print('\n\033[92;40mTenha uma boa noite!\033[49m')
