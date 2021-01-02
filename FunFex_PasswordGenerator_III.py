# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:01:02 2020

@author: user
"""
from time import sleep
from random import choice

def passwordGenerator(size, tipo):
    
    if tipo == 'num':
        numPassword = ''
        numChoices = '0123456789'
        
        for i in range(0, size):
            choosedChar = choice(numChoices)
            numPassword = numPassword + choosedChar
        
        print(f'  |Your numeric password is {numPassword}|')
        
    
    if tipo == 'alpha':

        alphaPassword = ''
        alphaChoices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for i in range(0, size):
            choosedChar = choice(alphaChoices)
            alphaPassword = alphaPassword + choosedChar
            
        print(f'  |Your alpha password is {alphaPassword}|')
    
    
    if tipo == 'alphanum':
        alphanumPassword = ''
        alphanumChoices = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for i in range(0, size):
            choosedChar = choice(alphanumChoices)
            alphanumPassword = alphanumPassword + choosedChar
            
        print(f'  |Your alphanum password is {alphanumPassword}|')
        
        
    if tipo == 'especial':
        especialPassword = ''
        especialChoices = '!@#$%¨&*()_-=+|\{[]}:;.,><?/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        
        for i in range(0, size):
            choosedChar = choice(especialChoices)
            especialPassword = especialPassword + choosedChar
            
        print(f'  |Your especial password is {especialPassword}|')
        
            
            
def menu():
    print('-'*92)
    print()
    print()
    print('FunFex Software')
    sleep(1)
    print('Initializing .../')
    sleep(5)
    
    print()
    
    print('+', '-'*90, '+')
    print('                                 FUNFEX  PASSWORD  GENERATOR   III ')
    print('+', '-'*90, '+')
    print()
    print('    Welcome to the FunFex Password Generator III !')
    
    sleep(1)
    
    print('           ', '_'*28)
    print('           |TO                     PRESS|')
    print('           |Generate password          P|')
    print('           |Exit                       E|')
    print('           |                            |')
    
    print()
    
    decision = input('  Your decision: ')
    
    if decision in ['E', 'e']:
        
        print()
        print('_'*92)
        print('  ...Thank you for using FunFex software...')
        print()
        sleep(1)
        print('  Shutting down .../')
        sleep(5)
        print()
        print('_'*92)
        input('Press enter key to exit ;')
        
    elif decision in ['P', 'p']:
        print()
        sleep(1)
        
        print('  |...The computer will generate a password for you ...|')
        sleep(2)
        print('  |...But...|')
        sleep(2)
        print('  |...We neeed some preferences first...|')
        sleep(2)
        
        print()
        
        print('_'*94)
        
        print('          **   Password   Preferences **')
        
        print()
        
        
        size = int(input('  [1]-How long will your password be ? [5-50]: '))
        tipo = input('  [2]-What will be type of your password ?[num, alpha, alphanum]: ')
        sleep(3)
        print()
        print('_'*92)
        print()
        
        for i in range(5, 0, -1):
            print()
            print('  |Generating password|')
            print(f'  |{i} seconds left|')
            sleep(1)
        
        sleep(1)
        print()
        print('_'*92)
        print()
        
        
        passwordGenerator(size, tipo)
        print()
        print('  |Save this and do not share|')
        print()
        print('_'*92)
        print()
        sleep(10)
        
        print('  ...Thank you for using FunFex software...')
        print()
        sleep(1)
        print('  Shutting down .../')
        sleep(5)
        print()
        print('_'*92)
        input('Press enter key to exit ;')
        
    else:
        sleep(5)
        print()
        print('_'*92)
        print()
        sleep(5)
        print('  ErrorMsg: |An error was found|')
        sleep(2)
        print('  The sistem is rebooting .../...')
        sleep(10)
        print()
        print('_'*92)
        sleep(1)
        menu()


menu()
