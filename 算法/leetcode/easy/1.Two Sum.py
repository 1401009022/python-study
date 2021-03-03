#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
class Sulution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i], i ]]




        # for i in nums:
        #     j = target - i
        #     start_index = nums.index(i)
        #     next_index = start_index +1
        #     temp_nums = nums[next_index:]
        #     if j in temp_nums:
        #         return (nums.index(i), next_index+temp_nums.index(j))


























