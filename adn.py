#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    documentation here
"""

__author__ = 'Louai KASSA BAGHDOUCHE'



def is_valid(adn_str):
    
    counter = 0

    for i in adn_str.lower(): 
        if i == 'a' or i == 'c' or i == 'g' or i == 't':
            counter += 1 

    return True if len(adn_str) == counter else False

def get_valid_adn(prompt='chaîne : '):
    
    valid = False
    while not valid:
        dna = input('Entrez une chaîne valide: ')
        valid = is_valid(dna)


get_valid_adn()
