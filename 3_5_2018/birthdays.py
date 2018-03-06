#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 14:50:45 2018

@author: davidnelson
"""

# This script updates a repository of birthdays

birthdays = {'Britney': 'December 2', 'Beyoncé': 'September 4', 
             'Mariah': 'March 27'}

def get_birthday():
    '''
    This function gets info from the birthday database or will update
    the database if the name entered is not found
    '''
    name = input('Whose birthday would you like to know? ')
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}.') 
    else:
        print(f'I do not have the birthday for {name}.')
        new_birthday = input(f"What is {name}'s birthday? ")
        birthdays.update({name: new_birthday})
        print('Birthday database updated. ')
    
get_birthday()

print(birthdays)
