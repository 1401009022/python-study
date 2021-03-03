#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 建立字典
        number_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)):
            # 怎么取字符串的一个呢？
            if i > 0 and number_map[s[i]] > number_map[s[i-1]]:
                result += number_map[s[i]] - 2 * number_map[s[i-1]]
            else:
                result += number_map[s[i]]

        return result

















