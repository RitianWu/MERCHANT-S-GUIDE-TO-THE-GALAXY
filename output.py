#!/usr/local/bin/python
# coding=utf-8

import re
from load_file import load_file

"""
Description: Output the results
Auth: Hao
Data: 2016-2-25
"""


def output(file_name, answer_roman, answer_price, unknown):
    """
    Print the result for conditions and questions in the task
    """

    answers = []

    # Loading task and print out
    print "Input:"
    for line in open(file_name):
        print line.strip('\n')

        if re.search(r'^how much is', line):
            line_list = line.strip('\n').split(' ')
            index_is = line_list.index('is')
            key_info = ' '.join(line_list[index_is + 1: len(line_list) - 1])
            answers.append("{key} is {value}".format(
                    key=key_info, value=answer_roman[key_info]))

        elif re.search(r'^how many Credits is', line):
            line_list = line.strip('\n').split(' ')
            index_is = line_list.index('is')
            key_info = ' '.join(line_list[index_is + 1: len(line_list) - 2])
            answers.append("{key} is {value} Credits".format(
                    key=key_info, value=answer_price[line_list[len(line_list) - 2]][key_info]))

        elif line in unknown:
            answers.append(
                "I don't know what the hell are you talking about...")

    # Output the result
    print "Output:"
    for result in answers:
        print result
