print('\033[1;97m-' * 26)
print('| \033[91mSEQUÊNCIA DE FIBONACCI \033[97m|')
print('-' * 26)
n = 0
while n <= 0:
    n = int(input('Quantos termos você quer mostrar? '))
    if n <= 0:
        print('Tente um número maior.\n')
t1 = 0
t2 = 1
t3 = 1
cont = 3
if n == 1:
    print('\n{} \033[91m➝ '.format(t1), end='')
elif n == 2:
    print('\n{} \033[91m➝ \033[97m{} \033[91m➝ '.format(t1, t2), end='')
elif n >= 3:
    print('\n{} \033[91m➝ \033[97m{} \033[91m➝ \033[97m{} \033[91m➝ '.format(t1, t2, t3), end='')
while cont < n:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print('\033[97m{} \033[91m➝ '.format(t3), end='')
    cont += 1
print('\033[91mFIM')
