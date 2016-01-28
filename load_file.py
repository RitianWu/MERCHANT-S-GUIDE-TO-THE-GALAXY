#!/usr/local/bin/python
# coding=utf-8

import re

"""
Description: Loading and analysis content from the task file
Auth: Hao
Data:2016-2-23
"""


def load_file(file_name):
    """
        Loading module
        Reading and analysis the task file, return 4 types of infos:
        condition_roman, dict, {'glob': 'I', ...}
        condition_price, nested dict, {'Silver': {'glob glob': 34}, ...}
        question_roman, dict, {'pish tegj glob glob': ''}
        question_price, nested dict, {'Silver': {'glob prok': 0}, ...}
    """

    # condition line from task file
    condition_roman = {}
    condition_price = {}
    # question line from task file
    question_roman = {}
    question_price = {}

    for line in open(file_name):
        if re.search(r'[IXVLCDM]$', line):
            # conditon roman analysis
            line_list = line.strip('\n').split(' ')
            condition_roman[line_list[0]] = line_list[-1]
        # elif re.search(r'\d* Credits', line):
        # 	# conditon price analysis
        # 	pass
        # elif re.search(r'^how much is', line):
        # 	# question roman
        # 	pass
        # elif re.search(r'^how many Credits is', line):
        # 	# question price
        # 	pass

    return condition_roman, condition_price, question_roman, question_price


if __name__ == "__main__":
    load_file("task.txt")
