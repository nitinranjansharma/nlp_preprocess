#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:54:39 2020

@author: poomahaj
"""


import unidecode

class RepAccentChar():
    def __init__(self,text):
        self.text=text
        
    def get_data(self):
        return(unidecode.unidecode(self.text))

def rep_accent_char(text):
    accent_char=RepAccentChar(text)
    return(accent_char.get_data())
