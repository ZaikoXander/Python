num = int(input('\033[1;94mDigite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[93m', end='')
        tot += 1
    else:
        print('\033[91m', end='')
    print('{} '.format(c), end='')
print('\n\033[96mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele \033[95mÉ PRIMO.')
else:
    print('E por isso ele \033[95mNÃO É PRIMO.')
