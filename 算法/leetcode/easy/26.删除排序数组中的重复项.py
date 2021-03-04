#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 考虑不存在的情况
        if not nums:
            return 0
        # 计数
        count = 0  # 不用1是因为只有一个的话会出问题
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count+1




        # flag = 1
        for i in nums:
            if nums[i] == nums[i+1] and nums[i] != nums[i+2]:
                flag = i
            elif nums[i] != nums[i+1]:
                nums[flag] = nums[i]
        return flag+1


























