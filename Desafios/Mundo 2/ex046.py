from time import sleep
import emoji
print('\033[95m>--<' * 8)
print('\033[91m Estouro de Fogos de Artifício')
print('\033[95m>--<' * 8 + '\n\033[93m')
for cont in range(10, 0, -1):
    print(cont, end=', ')
    sleep(1)
print('0...')
sleep(1)
print('\n' + '\033[90m-' * 9)
print('|\033[96m 00:00 \033[90m|')
print('-' * 9)
print('\033[94mFeliz Ano Novo!!!')
print(emoji.emojize('\033[95mBOoomm :fireworks:'))
