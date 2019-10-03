n = float(input('INSIRA UM NUMERO:'))
n_2 = float(input('INSIRA MAIS UM NUMERO'))
n_3 = float(input('INSIRA OUTRO NUMERO:'))
if n >= n_2 and n >= n_3:
    print(n)
    if n_2 >= n_3:
        print(n_2)
        print(n_3)
    else:
        print(n_3)
        print(n_2)
elif n_2 >= n_3:
    print(n_2)
    if n >= n_3:
        print(n)
        print(n_3)
    else:
        print(n_3)
        print(n)
else:
    print(n_3)
    if n >= n_2:
        print(n)
        print(n_2)
    else:
        print(n_2)
        print(n)
        
