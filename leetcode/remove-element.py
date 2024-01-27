class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                count+=1
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != "_":
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
            seeker += 1
        return len(nums)-count

            