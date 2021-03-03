#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

class Solution(object):
    def isPalindrome(self, x ):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False  #这个会不会提升效率？
        num = 0
        a = abs(x)
        while (a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)
        if x == num:
            return True
        else:
            return False



        # 为什么超时了。。  负数？ 对头，加上abs成功了！！
        revx = 0
        x1 = x  # 需要有一个保留原始数据
        x = abs(x)
        while (x != 0):
            b = x % 10
            print('b: ',b)
            revx = revx * 10 + b
            print('revx: ',revx)
            x = x //10
        if revx == x1:
            return True
        else:
            return False
