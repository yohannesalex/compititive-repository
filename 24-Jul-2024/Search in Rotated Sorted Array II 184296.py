# Problem: Search in Rotated Sorted Array II - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums_set: List[int], target: int) -> bool:
        
        n = len(nums_set)
        low = 0
        high = n - 1
        while(low <= high):
            mid = (low + high) // 2
            if nums_set[mid] == target:
                return True
            if nums_set[low] == nums_set[mid] and nums_set[mid] == nums_set[high]:
                low +=1
                high -= 1
                continue
            if nums_set[low] <= nums_set[mid]:
                if nums_set[low] <= target <= nums_set[mid]:

                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums_set[mid]<=target <= nums_set[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


        