class Solution:
    def smallestNumber(self, num: int) -> int:
        stri=[]
        nums=str(num)
        for  i in nums:
            stri.append(i)
        if num < 0:
            stri.remove(stri[0])
            stri.sort(reverse = True)
            return int('-'+"".join(stri))
        else:
            stri.sort()
            for i in range(len(stri)):
                if stri[i] != "0":
                    stri[i] , stri[0] = stri[0] , stri[i]
                    break
            return int("".join(stri))


