nota = float(input('INSIRA UMA NOTA: '))
nota_2 = float(input('INSIRA OUTRA NOTA: '))
media = (nota+nota_2)/2
if media < 7:
    print('SUA MÉDIA FOI DE', media, 'REPROVADO')
elif media > 7:
    print('SUA MEDIA FOI DE', media, 'APROVADO')
elif media == 10.0:
    print('APROVADO COM DISTINÇÃO')
print('fim')

