#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 整数倒序。。可是怎么整啊。。怎么表示每个数字呢
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        a = abs(x)  # abs() return the absolute value of a number
        # 就是不管符号，
        # while (a != 0):
        #     # 123  a = 123 num = 0
        #     # 求余法来。。
        #     # iteration
        #     i = 0
        #     b = a % 10
        #     a = (a - b) / 10
        #     num = num +  b * 10 * i
        # print(num)
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a / 10)   # 或者 a // 10
            # 不加int 不整除会导致有小数，一直除，超时  python3要这样
            # // 整除效率更高！

        # 正负  界限
        if x > 0 and num < 2147483647:  # 万一不知道这个数怎么办
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0



















