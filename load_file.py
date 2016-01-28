#!/usr/local/bin/python
# coding=utf-8

import re

"""
Description: Loading and analysis content from the task file
Auth: Hao
Data: 2016-2-23
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
    # unknown
    unknown = []

    for line in open(file_name):
        # conditon roman analysis
        if re.search(r'[IXVLCDM]$', line):
            line_list = line.strip('\n').split(' ')
            condition_roman[line_list[0]] = line_list[-1]
        # conditon price analysis
        elif re.search(r'is \d* Credits', line):
            line_list = line.strip('\n').split(' ')
            index_is = line_list.index('is')
            condition_price.setdefault(line_list[
                index_is - 1], {' '.join(line_list[0:index_is - 1]): int(line_list[index_is + 1])})
        # question roman
        elif re.search(r'^how much is', line):
            line_list = line.strip('\n').split(' ')
            index_is = line_list.index('is')
            question_roman[
                ' '.join(line_list[index_is + 1: len(line_list) - 1])] = ''
        # question price
        elif re.search(r'^how many Credits is', line):
            line_list = line.strip('\n').split(' ')
            index_is = line_list.index('is')
            question_price.setdefault(line_list[len(
                line_list) - 2], {' '.join(line_list[index_is + 1: len(line_list) - 2]): ''})
        # unknown
        else:
            # print "I don't know what the hell are you talking about..."
            unknown.append(line)
    # print condition_roman, condition_price, question_roman, question_price, unknown
    return condition_roman, condition_price, question_roman, question_price, unknown


if __name__ == "__main__":
    load_file("task.txt")
