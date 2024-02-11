class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = {}
        l = 0
        res = float("inf")
        for r,val in enumerate(cards):
            if val in window:
                res = min(res, r - window[val] + 1)
                l += 1
                window[val] = r
            window[val] = r
        if res != float("inf"):
            return res 
        else:
            return  -1
            