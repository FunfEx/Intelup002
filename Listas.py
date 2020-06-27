# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:24:26 2020

@author: user
"""

#criando uma lista
lista_do_mercado = ['ovos', 'farinha', 'leite', 'maças']
lista3 = [12, 100, 'Universidade']

#imprimindo uma lista
print(lista_do_mercado)


print('-'*10)


#atribuindo cada elemento da lista em varias variaveis
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]

print(item1, item2, item3)


print('-'*10)


#atualizando um item na lista

#imprimindo algum item na posição da lista
print(lista_do_mercado[0])


print('-'*10)


#atualizando e alterando um item na lista
#a palavra 'leite' foi excluida e 'chocolate' entrou no lugar
lista_do_mercado[2] = 'chocolate'
print(lista_do_mercado)


print('-'*10)


#deletando um item especifico na lista
del lista_do_mercado[3]   #deleta 'maças'
print(lista_do_mercado)


print('-'*10)


#listas de listas (listas aninhadas)

#criando uma lista de listas
lista_aninhada = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(lista_aninhada)


print('-'*10)


#atribuindo um item da lista a uma variavel
a = lista_aninhada[0]
print(a)


print('-'*10)


#se a = [1, 2, 3], então o numero 1 é a[0]
#vamos atribuir a[0] a uma variavel
b = a[0]
print(b)


print('-'*10)


list1 = lista_aninhada[1]
print(list1)


print('-'*10)


valor_1_0 = list1[0]
print(valor_1_0)


print('-'*10)


valor_1_2 = list1[2]
print(valor_1_2)


print('-'*10)


list2 = lista_aninhada[2]
print(list2)


print('-'*10)


valor_2_0 = list2[0]
print(valor_2_0)


print('-'*10)


#operações com listas

#atribuindo a variavel a o primeiro valor da primeira lista
print(lista_aninhada)


print('-'*10)


a = lista_aninhada[0][0]
print(a)


print('-'*10)


# o terceiro elemento da 2 lista
b = lista_aninhada[1][2]
print(b)


print('-'*10)


c = lista_aninhada[0][2] 
print(c)


print('-'*10)


#pega o valor da 2 pos da lista 0 e soma 10
c = lista_aninhada[0][2] + 10
print(c)


print('-'*10)


#pega o valor da lista 2 na pos 0 e multiplica por 10
d = 10
e =     d * lista_aninhada[2][0]
print(e)


print('-'*10)


print(lista_aninhada[2][0])



print('-'*10)


#concatenando listas
lista_s1 = [34, 32, 56]
print(lista_s1)

lista_s2 = [21, 90, 51]
print(lista_s2)


print('-'*10)


#concatenando
lista_total = lista_s1 + lista_s2
print(lista_total)


print('-'*10)


#operador in


lista_teste_op = [100, 2, -5, 3.4]

#verificando se o valor está na lista
print(10 in lista_teste_op)
print(100 in lista_teste_op)


print('-'*10)


#funções built-in

#len() retorna o comprimento da lista
print(len(lista_teste_op))


print('-'*10)


#função max() retorna o valor máximo da lista
print(max(lista_teste_op))


print('-'*10)


#min() retorna o valor minimo da lista
print(min(lista_teste_op))


print('-'*10)


#adicionando um valor na lista
lista_compras = ['carne', 'macarrão', 'leite']
lista_compras.append('bolacha')
print(lista_compras)


print('-'*10)


#criando uma lista vazia
lista_vazia = []
print(lista_vazia)

print(type(lista_vazia))


print('-'*10)


lista_vazia.append(10)
print(lista_vazia)


print('-'*10)


old_list = [1, 2, 5, 10]
new_list = []


#copiando os itens de uma lista p outra
for item in old_list:
    new_list.append(item)
    

print(new_list)



print('-'*10)


print(new_list.count(5))


nomes = ['Python', 'Git Hub', 'Data Science']

#.index() retorna qual a pos do item (começando por 0)
print(nomes.index('Git Hub'))


#remove um item
nomes.remove('Python')
print(nomes)


#reverte 
nomes.reverse()
print(nomes)



#.sort() coloca valores em ordem
w = [9, 8, 7, 6]
w.sort()
print(w)

