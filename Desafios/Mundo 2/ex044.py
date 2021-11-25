print(f'{" LOJAS LIMA ":=^40}')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = 0
while opcao <= 0 or opcao > 4:
    opcao = int(input('\nQual é a opção? '))
    if opcao <= 0 or opcao > 4:
        print('\nOpção inválida. Tente novamente!')
if opcao == 1:
    total = preco - preco * 0.1
elif opcao == 2:
    total = preco - preco * 0.05
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
else:
    total = preco + preco * 0.2
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
