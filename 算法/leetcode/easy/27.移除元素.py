#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 指针 指向开头 指向结尾
        # 第一个数字和最后一个互换
        # 删掉最后一个数字
        # round 1 3,2,2,3 变换后 after_swap 3,2,2,3
        # round 2   3,2,2,3=> 2,2,3,3 (最后一位已经没用
        # round 3   2,2,3,3 =》 2,2,3,3
        # round 4  => 2,2,3,3
        # round 5   return last+1

        i, last = 0, len(nums) - 1

        while i <= last:
            if nums[i] == val:
                nums[i],nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1
        return last + 1 # 注意加一！











nums = [0,1,2,2,3,0,4,2]
val = 2
flag = 0

for i in range(len(nums)):
    if nums[i] != val:
        print("第一个循环",flag)
        print(nums[i])
        flag += 1
    else:
        for j in range(i + 1, len(nums)): # 左闭右开
            if nums[j] != val:
                print("第二个：",flag)
                nums[flag] = nums[j]
                nums[j] = val
                flag += 1
                break #一定要break！！！！
                # print(flag)
                # print(nums)

print(flag)
