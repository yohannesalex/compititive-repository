class Solution:
    def longestPalindrome(self, s: str) -> int:
        dup = Counter(s)
        ans=0
        for i in dup:
            if dup[i] > 1 :
                if dup[i] %2 == 0:

                    ans+=dup[i]
                else:
                    ans+=(dup[i]-1)
        for i in dup:
            if dup[i]%2 != 0:
                ans+=1
                break
        return ans
