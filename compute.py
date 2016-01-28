#!/usr/local/bin/python
# coding=utf-8

from translater import Translater
from load_file import load_file

"""
Description: Computing the result with translater based on conditions and questions from the task
Auth: Hao
Data: 2016-2-24
"""


def compute(cond_roman, cond_price, ques_roman, ques_price):
    """
    Computing module
    Input:
    cond_roman, dict, {'glob': 'I', ...}
    cond_price, nested dict, {'Silver': {'glob glob': 34}, ...}
    ques_roman, dict, {'pish tegj glob glob': ''}
    ques_price, nested dict, {'Silver': {'glob prok': 0}, ...}
    Return:
    answer_roman, dict, {'pish tegj glob glob': ''}
    answer_price, nested dict, {'Silver': {'glob prok': 0}, ...}
    """

    answer_roman = ques_roman
    answer_price = ques_price
    price = {}  # 保存商品单价

    # 转为罗马数字表示
    translater = Translater(info_roman=cond_roman)
    for k in ques_roman.keys():
        answer_roman[k] = translater.translate_to_num(
            translater.translate_to_roman(k))

    # 计算单价
    for k, v in cond_price.iteritems():
        for info_roman in v.keys():
            price[k] = v[info_roman] / \
                float(translater.translate_to_num(
                    translater.translate_to_roman(info_roman)))
    # 计算结果
    for k, v in ques_price.iteritems():
        for info_roman in v.keys():
            answer_price[k][info_roman] = int(translater.translate_to_num(
                translater.translate_to_roman(info_roman)) * price[k])

    return answer_roman, answer_price


if __name__ == "__main__":
    cond_roman, cond_price, ques_roman, ques_price = load_file("task.txt")
    print compute(cond_roman, cond_price, ques_roman, ques_price)
