total = maismil = barato = cont = 0
nomebarato = ''
print('\033[1;97m-' * 18)
print('| \033[91mLoja do Xandão \033[97m|')
print('-' * 18)
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = ' '
    while not preco.isnumeric():
        preco = input('Preço: \033[93mR$')
    preco = int(preco)
    cont += 1
    total += preco
    if preco > 1000:
        maismil += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('\033[97mQuer continuar? [\033[91mS\033[97m/\033[91mN\033[97m] ')).strip().upper()[0]
    print()
    if opcao == 'N':
        break
print('{:-^28}'.format(' \033[91mResultados \033[97m'))
print('O total da compra foi \033[93mR${:.2f}'.format(total))
if maismil == 0:
    print('\033[97mTemos \033[91mnenhum \033[97mproduto custando mais de \033[93mR$1000.00')
elif maismil == 1:
    print('\033[97mTemos \033[91m1 \033[97mproduto custando mais de \033[93mR$1000.00')
else:
    print('\033[97mTemos \033[91m{} \033[97mprodutos custando mais de \033[93mR$1000.00'.format(maismil))
print('\033[97mO produto mais barato foi \033[91m{} \033[97mque custa \033[93mR${:.2f}'.format(nomebarato, barato))
