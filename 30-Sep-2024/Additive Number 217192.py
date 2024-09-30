# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]
                
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                num1, num2 = int(num1), int(num2)
                k = j
                
                while k < n:
                    num3 = num1 + num2
                    num3_str = str(num3)
                    if not num.startswith(num3_str, k):
                        break
                    k += len(num3_str)
                    num1, num2 = num2, num3

                if k == n:
                    return True
        
        return False
