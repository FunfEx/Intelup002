preco = float(input('INSIRA O PREÇO DE UM PRODUTO: '))
preco2 = float(input('INSIRA O PREÇO DE UM PRODUTO: '))
preco3 = float(input('INSIRA O PREÇO DE UM PRODUTO: '))
if preco < preco2 and preco < preco3:
    print('COMPRE O PRODUTO 1------', preco, 'R$')
elif preco2 < preco and preco2 < preco3:
       print('COMPRE O PRODUTO 2------', preco2, 'R$')
elif preco3 < preco and preco3 < preco2:
    print('COMPRE O PRODUTO 3------', preco3, 'R$')
else:
    print('----VALOR INVALIDO----')
