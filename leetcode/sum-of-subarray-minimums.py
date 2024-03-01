class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                if stack:
                    left= stack[-1]  
                else:

                    left =-1
                right = i

                count = (mid - left) * (right - mid) % MOD

                res += (count * arr[mid]) % MOD
                res %= MOD
            stack.append(i)

        return int(res)
        