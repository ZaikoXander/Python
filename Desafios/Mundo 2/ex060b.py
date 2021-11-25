print('\033[1;97m-' * 12)
print('| \033[91mFATORIAL \033[97m|')
print('-' * 12)
n = int(input('Digite um valor: '))
f = n
print('\n{}! \033[91m= '.format(n), end='\033[97m')
for c in range(n-1, 0, -1):
    f *= c
    if c > 1:
        print('{} \033[91mx '.format(c), end='\033[97m')
    else:
        print('{} \033[91m= {}\033[97m'.format(c, f))
