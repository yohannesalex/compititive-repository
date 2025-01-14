# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        countA = defaultdict(int)
        countB = defaultdict(int)
        count = 0
        ans = []
        for i in range(len(A)):
            countA[A[i]]+=1
            countB[B[i]]+=1
            if A[i] == B[i]:
                count+=1
            else:
                if countA[B[i]] != 0:
                    count+=1
                if countB[A[i]] != 0:
                    count+=1
            ans.append(count)
        return ans