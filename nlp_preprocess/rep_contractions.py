#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:58:48 2020

@author: poomahaj
"""


import contractions  

class RepContractions():
    def __init__(self,text):
        self.text=text
        
    def get_data(self):
        return(contractions.fix(self.text))

def rep_contractions(text):
    return(RepContractions(text).get_data())
    
