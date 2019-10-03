num = float(input('INSIRA UM NUMERO: '))
num2 =float(input('INSIRA UM NUMERO: '))
num3 = float(input('INSIRA UM NUMERO: '))

if num == num2 and num == num3:
    print('OS NUMEROS', num, ',', num2, 'e', num3, 'SÃO IGUAIS')
else:    
    if  num > num2 and num > num3:
        print('MAIOR É O', num)
    elif num2 > num and num2 > num3:
        print('MAIOR É O', num2)
    elif num3 > num and num3 > num2:
        print('MAIOR É O', num3)

        
    if num < num2 and num < num3:
        print('MENOR É O', num)
    elif num2 < num and  num2 < num3:
        print('MENOR É O', num2)
    elif num3 < num and num3 < num2:
        print('MENOR É O', num3)

