from time import sleep
velocidade = int(input('\033[1;95;40mQual a velocidade atual de um carro? '))
sleep(0.5)
print('\033[97mAnalisando.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.\033[49m')
sleep(1)
if velocidade > 80:
    print('\n\033[91;40mMULTADO! Você excedeu o limite permitido que é de 80Km/h!\033[49m')
    print('\033[40mVocê deve pagar uma multa de \033[93mR${:.2f}\033[91m!\033[49m'.format((velocidade - 80) * 7))
print('\n\033[92;40mTenha um bom dia! Dirija com segurança!\033[49m')
