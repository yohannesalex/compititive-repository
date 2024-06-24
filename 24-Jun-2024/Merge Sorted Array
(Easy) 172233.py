# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n2 = n
        for i in range(n):
            nums1[m + i] = nums2[n2 - 1]
            while n2 < 0:
                return
            n2 -= 1
        nums1.sort()