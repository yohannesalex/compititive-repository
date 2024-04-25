# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9+7
        dic = defaultdict(int)
        s1 = SortedList()
        sum_ = 0
        
        for i in range(len(instructions)):
            dic[instructions[i]] += 1
            s1.add(instructions[i])
            if i == 0:
                sum_ = (sum_+0)%mod
            else:
                leftIndex = s1.bisect_left(instructions[i])
                small = leftIndex - 0
                big = len(s1) - leftIndex
                if dic[instructions[i]]>0:
                    big -= dic[instructions[i]]
                sum_ = (sum_+min(small,big))%mod
        return sum_