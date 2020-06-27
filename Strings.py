# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:15:39 2020

@author: user
"""


#printando strings com quebra de linha
print('Testando \nStrings \nem \nPython')


print('-'*10)


#indexando strings
s = "Marcello"
print(s)

print(s[0])
print(s[1])
print(s[2])


print('-'*10)


#slicing: leitura de tudo até um ponto desejado
print(s[1:])
print(s[3:])


print('-'*10)


#indexação negativa le de tras p/ frente
print(s[-1])
print(s[:-1])


print('-'*10)


#concatenando strings
s = s + ' Belanda '
print(s)


#simbolo de multiplicação cria repetição
letra = 'w'
print(letra*10)


print('-'*10)

'''
funcoes built-in de strings
'''

#transformar as letras em maiúsculas
print(s.upper())


print('-'*10)


#transformar as letras em minusculas
print(s.lower())


print('-'*10)


#dividir uma string por espaços em branco
p = 'Eu gosto de repolho mas eu odeio banana'
print(s.split())


print('-'*10)


print(p.split())


#dividir uma string por um elemento especifico
print(s.split('a'))


print('-'*10)


#comparando strings
print('python' == 'R')
print('python' == 'python')


print('-'*10)


#funcoes string
a = 'seja bem-vindo ao universo de Python'

#Deixa maiusculo a primeira letra da string
print(a.capitalize())

#conta quantas vezes apareceu cada palavra ou caractere
print(a.count('seja'))
print(a.count('a'))

#retorna a posição do caractere 
print(a.find('Python'))
print(a.find('P'))

#verifica se é alfanumerico
print(a.isalnum())

#verifica se é letra
print(a.isalpha())

#verifica se é minusculo
print(a.islower())

#verifica se é maiuscula
print(a.isupper())

#verifica se termina com um certo caractere
print(a.endswith('n'))



































