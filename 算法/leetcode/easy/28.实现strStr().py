#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 问题：怎么挨个取出字符串的字符进行比较呢？
        # 解决：利用截取 分片

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)]  == needle:
                return i

        return -1













