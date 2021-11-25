num = int(input('\033[1;95;40mDigite um valor: '))
if num < 10:
    print('\033[49m\n\033[91;40m - Tabuada do {} -  \033[49m'.format(num))
elif num < 100:
    print('\033[49m\n\033[91;40m - Tabuada do {} - \033[49m'.format(num))
elif num < 1000:
    print('\033[49m\n\033[91;40m- Tabuada do {} - \033[49m'.format(num))
else:
    print('\033[49m\n\033[91;40m- Tabuada do {} -\033[49m'.format(num))
print('\033[94;40m=\033[49m' * 19)
for c in range(1, 10):
    print('\033[93;40m|\033[22;39m{:>4} x {} = {:<6}\033[1;93m|\033[49m'.format(num, c, num * c))
print('\033[40m|\033[22;39m{:>4} x 10 = {:<5}\033[1;93m|\033[49m'.format(num, num * 10))
print('\033[94;40m=\033[49m' * 19)
