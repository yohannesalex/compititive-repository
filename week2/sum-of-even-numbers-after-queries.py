class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        func = lambda a: not(a % 2)
        x = filter(func, nums)
        ans = []
        s = sum(list(x))
        for q in queries:
            value = nums[q[1]]
            if not nums[q[1]] % 2:
                nums[q[1]] += q[0]
                if not nums[q[1]] % 2:
                    s += q[0]
                    ans.append(s)
                else:
                    s -= value
                    ans.append(s)
            else:
                nums[q[1]] += q[0]
                if not nums[q[1]] % 2:
                    s += nums[q[1]]
                    ans.append(s)
                else:
                    ans.append(s)
        return ans

