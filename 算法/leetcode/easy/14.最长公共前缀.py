#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 自己在做的时候没解决的问题
        # 1.如何确定这里面最短的字符串
        # 2.如何得到每个字符串的具体某个字符 从而进行比较
        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result













        if not strs:
            return "" #???干啥用的
        for i in range(len(strs[0])):
            # strs[0][i] ?= strs[1][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]


















        strs = ["flower","flow","flight"]
        # print(strs[:-1])
        retstr = ""
        for i in range(0, len(strs)):
            for j in strs[:-1]:

                if j == j:
                    print(j[i])
                    if j+1 == len(strs):
                        retstr = retstr + j[i]
                        print(retstr)
                elif i == len(strs) -1:
                    if retstr =="":
                        print("")
                    else:
                        print(retstr)

a = Solution()
a.longestCommonPrefix()