class Solution:
    def balancedString(self, s: str) -> int:
        extra=""
        actual=len(s)//4
        count=Counter(s)
        for ch in count:
            if count[ch]>actual:
                extra+=(count[ch]-actual)*ch
        if not extra:
            return 0
        count1=Counter(extra)
        left=0
        ans=inf
        freq=Counter()
        for right,ch in enumerate(s):
            freq[ch]+=1
            while count1-freq==Counter():
                ans=min(ans,right-left+1)
                freq[s[left]]-=1
                left+=1     
        return ans
            
        