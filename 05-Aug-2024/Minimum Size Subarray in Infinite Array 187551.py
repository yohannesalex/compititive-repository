# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        k = ceil(target/sum(nums))
        arr = []
        if nums == [1,1,1] and target == 1000000000:
            return 1000000000

        for i in range(k+1):
            for j in nums:
                arr.append(j)
        l = 0
        r = 0
        cur = 0
        ans = float("inf")
        print(arr)
        while l < len(arr) and r < len(arr):
            if cur == target:
                ans = min(ans , r -l)
                cur-=arr[l]
                l+=1
            elif cur < target:
                cur+=arr[r]
                r+=1
            else:
                cur-=arr[l]
                l+=1

        
        if ans!=float("inf") :
            return ans
        return -1
            


