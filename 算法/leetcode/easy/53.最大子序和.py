#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Solution(object):
    def maxSubArray(self, nums =[-2,1,-3,4,-1,2,1,-5,4]):
        """
        :type nums: List[int]
        :rtype: int
        """

        if max(nums) < 0:
            return max(nums)

        local_max, global_max =0 , 0

        for num in nums:
            local_max =  max(0, local_max + num)
            global_max = max(global_max, local_max)

        return global_max










        # 通过了，但是运行速度太慢
        maxnum = nums[0]  # 不能设置为0 万一最大的是负数呢
        temp = 0
        for i in range(len(nums)):
            if nums[i] > maxnum:
                maxnum = nums[i]
                print(maxnum)
            if i < len(nums):
                for j in nums[i:]:  # i开始
                    temp = temp+j
                    if temp > maxnum:
                        maxnum = temp
            temp = 0
        return maxnum

a = Solution()
a.maxSubArray()