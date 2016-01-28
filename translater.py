#!/usr/local/bin/python
# coding=utf-8

import re
from config import *

"""
Description: The translation between Romans and Numbers
Auth: Hao
Data:2016-2-22
"""


class Translater(object):

    def __init__(self):
        """ Init for Translater
        """
        self.__roman_num = Roman_Num
        self.__info_roman = Info_Roman

    def __check_roman_info(self, roman_str):
        """ check the validity of roman string
        """
        return roman_str if re.search(regex_roman, roman_str) else None

    def translate_to_roman(self, info_str):
        """ Translate a given number to Roman string
            Input: "glob prok"
            Output: "IV"
        """
        roman_list = [self.__info_roman.get(
            key, " ") for key in info_str.strip().split()]
        if " " in roman_list:
            return None
        return "".join(roman_list)

    def translate_to_num(self, roman_str):
        """ Translate a given Roman string to number
            Input: "MCMIII"
            Output: "1903"
        """
        sum = 0
        if self.__check_roman_info(roman_str):
            for i in range(len(roman_str) - 1):
                if Roman_Num[roman_str[i + 1]] > Roman_Num[roman_str[i]]:
                    sum = sum - Roman_Num[roman_str[i]]
                else:
                    sum = sum + Roman_Num[roman_str[i]]
            sum = sum + Roman_Num[roman_str[len(roman_str) - 1]]
        return sum
