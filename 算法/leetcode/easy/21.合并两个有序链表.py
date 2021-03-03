#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 但是这样最后会指向最后 多加一个就好了
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2

        return dummy.next




        l3 = []
        if l1 == [] or l2 == []:
            return l1 if l1 == [] else l2

        while l1.val != None:
            if l1.val >= l2.val:
                l3.append(l2.val)
                l2 = l2.next
            else:
                l3.append(l1.val)
                l1 = l1.next
        if l2.val != None:
            l3.append(l2)
        return l3

        l3 = []
        if l1 == [] or l2 == []:
            return l1 if l1 == [] else l2
        # 找出他们的长度来
        maxlength = len(l1) if len(l1) >= len(l2) else len(l2)
        for i in range(0, len(l1)):
            if l1.val >= l2.val:
                l3.append(l2.val)
                l2 = l2.next
            else:
                l3.append(l1.val)
                l1 = l1.next
        return l3
