#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:55:40 2020

@author: poomahaj
"""


class NonEnglishScript():
    def __init__(self, text):
        self.text = text
        

    def get_data(self):
        return(' '.join([i for i in self.text.split(" ") if i.isascii()]))


def rem_nonenglishscript(text):
    rem_noneng = NonEnglishScript(text)
    return rem_noneng.get_data()
