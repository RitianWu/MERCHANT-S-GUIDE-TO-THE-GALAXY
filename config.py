#!/usr/local/bin/python
# coding=utf-8

"""
Desc: the basic info for translater configuration
"""

Roman_Num = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

Info_Roman = {
    "glob": "I",
    "prok": "V",
    "pish": "X",
    "tegj": "L"
}

regex_roman = "^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
