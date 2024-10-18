# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def findbit(arr):
            k = 0
            for i in arr:
                k = k | i
            return k
        def all_combinations(arr):
            # Base case: return an empty combination if the array is empty
            if len(arr) == 0:
                return [[]]
            
            rest_combinations = all_combinations(arr[1:])
            
            with_first = [[arr[0]] + comb for comb in rest_combinations]
            
            return with_first + rest_combinations
        combArr = all_combinations(nums)
        counter = defaultdict(int)
        for arr in combArr:
            cur = findbit(arr)
            counter[cur]+=1
        maxi = 0
        for key , val in counter.items():
            maxi = max(maxi, key)
        return counter[maxi]


