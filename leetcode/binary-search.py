class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.mid = (len(nums))//2
        def binary(l,r):
            if l == r and nums[l]!= target:
                return -1
            if nums[self.mid] == target:
                return self.mid
            elif nums[self.mid] < target:
                l = self.mid+1
            else:
                r = self.mid-1
            self.mid=(l+r)//2
            return binary(l,r)
        return binary(0,len(nums)-1)