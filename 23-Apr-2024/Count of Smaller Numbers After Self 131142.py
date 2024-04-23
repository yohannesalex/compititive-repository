# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        track = []
        for i in range(len(nums)):
            track.append([nums[i], i])
        def merger(leftArr, rightArr):
            leftInd = 0
            rightInd = 0
            sortedarr = []
            while leftInd < len(leftArr) and rightInd < len(rightArr):
                if leftArr[leftInd][0] <= rightArr[rightInd][0]:
                    sortedarr.append(leftArr[leftInd])
                    counts[leftArr[leftInd][1]] += rightInd 
                    leftInd += 1
                else:
                    sortedarr.append(rightArr[rightInd])
                    rightInd += 1
            
            while leftInd < len(leftArr):
                    sortedarr.append(leftArr[leftInd])
                    counts[leftArr[leftInd][1]] += rightInd 
                    leftInd += 1
            while rightInd < len(rightArr):
                sortedarr.append(rightArr[rightInd])
                rightInd += 1

            return sortedarr

        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            leftArr = mergeSort(left, mid, arr)
            rightArr = mergeSort(mid + 1, right, arr)

            return merger(leftArr, rightArr)

        mergeSort(0, len(nums) -1, track)
        return counts

