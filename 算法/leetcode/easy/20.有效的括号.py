#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 问题：这个怎么表示呢？用栈？！
        stack = []
        lookup = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            # 右边不在的时候开始寻找匹配  {[]}
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
            # 还有一种情况，就是只有一个，比如 s = "]"

        # 不是直接return True

        return len(stack) == 0





















