#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 怎么解决第一位和最后一位的问题
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i  # ?????





        # 自己的！解题成功！
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target > nums[i] and i < len(nums) - 1 and target < nums[i + 1]:
                return i + 1
            elif target == nums[i]:
                return i - 1
        if target <= nums[0]:
            return 0
        else:
            return len(nums)
















