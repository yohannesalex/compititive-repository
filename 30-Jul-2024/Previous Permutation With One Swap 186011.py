# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,0,-1):
            if arr[i]<arr[i-1]:
                ind=i-1
                break
        else:
            return arr
        m=ind+1
        for i in range(ind+1,len(arr)):
            if arr[m]<arr[i] and arr[ind]>arr[i]:
                m=i
        arr[m],arr[ind]=arr[ind],arr[m]
        return arr