#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        local_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count
        return count









        if s == None:
            return 0
        elif " " not in s:
            return len(s)
        s = list(s)
        s.reverse()
        for i in range(len(s)):
            if s[i] == " ":
                return i

a = Solution()
a.lengthOfLastWord("a ")