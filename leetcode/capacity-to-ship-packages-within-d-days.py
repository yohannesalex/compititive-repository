class Solution:
    def shipWithinDays(self, nums: List[int], k: int) -> int:
        def check(n):
            store_count=0
            count=0
            for i in nums:
                if store_count + i> n:
                    
                    store_count=0
                    count+=1
                store_count+=i
            return count < k
        l=max(nums)
        r = sum(nums)
        mini=float("inf")
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                mini=min(mini,mid)
                r = mid-1
            else:
                l = mid+1
        return mini


