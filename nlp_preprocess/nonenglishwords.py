#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:57:21 2020

@author: poomahaj
"""


import nltk
#nltk.download('words')  

class NonEnglishWords():
    def __init__(self,text,words,rem):
        self.text = text
        self.words=words
        self.rem=rem
        

    def get_data(self):
        if self.rem:
            return(' '.join([i for i in self.text.split(" ") if i.lower() in self.words]))
        else:
            return(' '.join([i for i in self.text.split(" ") if i.lower() not in self.words]))
            
        

def nonenglishwords(text,rem=True):
    words = set(nltk.corpus.words.words())
    rem_noneng = NonEnglishWords(text,words,rem)
    return rem_noneng.get_data()
