#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s 为空

        start = -1
        max = 0
        d = {}

        for i in range(len(s)):
            # s[i] in d...
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            # s[i] not in d...
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i - start

        return max


















