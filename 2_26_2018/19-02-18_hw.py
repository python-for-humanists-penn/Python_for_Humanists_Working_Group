#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:38:22 2018

@author: davidnelson
"""

# This provides a special response if a user responds "great" regardless
# of case or added white space
def how_are_you():
    '''
    Asks the user how they are doing and returns
    a special response if they say great.
    '''
    answer = input('How are you? ')
    if answer.lower().strip() == 'great':
        print('Have a great day!')
    else:
        print("That's not so great...")

how_are_you()

# This will also provide a special response if a user responds great, but
# will sass the user if they include extra white space

def how_you_doing():
    '''
    Asks the user how they are doing and returns
    a special response if they say great.
    '''
    answer = input('How are you? ')
    if answer.lower() == 'great':
        print('Have a great day!')
    elif answer.strip() != answer:
        print('Whoa, space cadet...')
    else:
        print("That's not so great...")

how_you_doing()