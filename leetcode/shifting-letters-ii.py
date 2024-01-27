class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dup = [0]*(n + 1)
        res = ""
        for x,y,z in shifts:
            if z:
                dup[x] += 1
                dup[y + 1] -= 1
            else:
                dup[x] -= 1
                dup[y + 1] += 1
                    

        for i in range(1, n):
            dup[i] += dup[i - 1]
    
        for j in range(n):
            res += chr((ord(s[j]) - ord('a') + dup[j]) % 26 + ord('a'))
        
        return res