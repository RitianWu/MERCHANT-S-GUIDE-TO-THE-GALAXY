#!/usr/local/bin/python
# coding=utf-8

from load_file import load_file
from compute import compute
from output import output


"""
Description: 程序入口
Auth: Hao
Data: 2016-2-25
"""

def main():
    """ 主函数
    """
    # 语义理解部分，读取文本信息，提取条件和问题
    cond_roman, cond_price, ques_roman, ques_price, unknown = load_file("task.txt")
    # 逻辑运算部分，根据条件和问题，计算结果
    answer_roman, answer_price = compute(cond_roman, cond_price, ques_roman, ques_price)
    # 结果输出部分，按照规则描述进行输出
    output("task.txt", answer_roman, answer_price, unknown)


if __name__ == "__main__":
    main()
