#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            nums3 = []

            # 要考虑特殊情况，
            markb = 0
            for i in range(len(nums1)):
                

