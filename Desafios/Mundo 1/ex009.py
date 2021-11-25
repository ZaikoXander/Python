num = int(input('\033[1;95;40mDigite um valor: '))
if num <= 10:
    print('\033[49m\n\033[91;40m - Tabuada do {} - \033[49m'.format(num))
elif num <= 100:
    print('\033[49m\n\033[91;40m - Tabuada do {} -\033[49m'.format(num))
else:
    print('\033[49m\n\033[91;40m- Tabuada do {} -\033[49m'.format(num))
print('\033[94;40m=\033[49m' * 19)
print('\033[93;40m|\033[22;39m{:>4} x 1 = {:<6}\033[1;93m|\033[49m'.format(num, num * 1))
print('\033[40m|\033[22;39m{:>4} x 2 = {:<6}\033[1;93m|\033[49m'.format(num, num * 2))
print('\033[40m|\033[22;39m{:>4} x 3 = {:<6}\033[1;93m|\033[49m'.format(num, num * 3))
print('\033[40m|\033[22;39m{:>4} x 4 = {:<6}\033[1;93m|\033[49m'.format(num, num * 4))
print('\033[40m|\033[22;39m{:>4} x 5 = {:<6}\033[1;93m|\033[49m'.format(num, num * 5))
print('\033[40m|\033[22;39m{:>4} x 6 = {:<6}\033[1;93m|\033[49m'.format(num, num * 6))
print('\033[40m|\033[22;39m{:>4} x 7 = {:<6}\033[1;93m|\033[49m'.format(num, num * 7))
print('\033[40m|\033[22;39m{:>4} x 8 = {:<6}\033[1;93m|\033[49m'.format(num, num * 8))
print('\033[40m|\033[22;39m{:>4} x 9 = {:<6}\033[1;93m|\033[49m'.format(num, num * 9))
print('\033[40m|\033[22;39m{:>4} x 10 = {:<5}\033[1;93m|\033[49m'.format(num, num * 10))
print('\033[94;40m=\033[49m' * 19)
