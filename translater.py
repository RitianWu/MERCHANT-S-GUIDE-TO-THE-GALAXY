#!/usr/local/bin/python
# coding=utf-8

import re
from config import Roman_Num, Info_Roman, regex_roman

"""
Description: The translation between Romans and Numbers
Auth: Hao
Data:2016-2-22
"""


class Translater(object):

    def __init__(self, roman_num=None, info_roman=None):
        """ Init for Translater
        """
        self.__roman_num = roman_num if roman_num else Roman_Num
        self.__info_roman = info_roman if info_roman else Info_Roman

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
                if self.__roman_num[roman_str[i + 1]] > self.__roman_num[roman_str[i]]:
                    sum = sum - self.__roman_num[roman_str[i]]
                else:
                    sum = sum + self.__roman_num[roman_str[i]]
            sum = sum + self.__roman_num[roman_str[-1]]
        else:
            print "the roman string is invalid!"
        return sum
