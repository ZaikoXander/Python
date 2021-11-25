while True:
    n = int(input('\033[1;97mQuer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=' * 19)
    for c in range(1, 11):
        if c == 10:
            print('|\033[91m{:>4} \033[97mx \033[91m{} \033[97m= \033[91m{:<5}\033[97m|'.format(n, c, n * c))
            break
        print('|\033[91m{:>4} \033[97mx \033[91m{} \033[97m= \033[91m{:<6}\033[97m|'.format(n, c, n * c))
    print('=' * 19 + '\n')
print('{:-^30}'.format('TABUADA FINALIZADA'))
