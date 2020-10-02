# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:40:03 2020

@author: user
"""


from random import choice
from time import sleep


def menu_resultado():
    print("+--------------------------")
    print('[|SEUS DADOS|]')
    print('|Nome de usuário: [{}]'.format(user))
    print('|Senha: [{}]'.format(senha))
    print('|Número de caracteres da sua senha: [{}]'.format(tamanho_senha))
    print("+--------------------------")
    
    

caracteres  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYX123456789!@#*+=-'
seleção = choice(caracteres)

print('-'*10)

user = input('|DIGITE O NOME DO USUÁRIO| : ')
tamanho_senha = int(input('|QUANTOS CARACTERES VOCÊ QUER QUE ESTEJAM PRESENTES NA SUA SENHA ?| :'))

senha = ''

for i in range(0, tamanho_senha+1):
    
    senha += choice(caracteres)
    
    
    
for i in range(10, -1, -1):
    sleep(1)
    print('|GERANDO SENHA.', i, 'SEGUNDOS RESTANTES ...|')


menu_resultado()




 
