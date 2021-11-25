from time import sleep
num = int(input('\033[1;95;40mDigite um número: '))
sleep(1)
# if num % 2 == 0:
if num % 2:
    print('\033[49m\n\033[94;40mO número {} é \033[91mÍMPAR\033[94m.\033[49m'.format(num))
else:
    print('\033[49m\n\033[94;40mO número {} é \033[91mPAR\033[94m.\033[49m'.format(num))
