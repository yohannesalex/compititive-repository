# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBra = 0
        closeBra = 0
        ans = 0
        stack = []
        for i in s:
            if i == '(':
                openBra +=1
                stack.append(i)
            if i == ')':
                closeBra+=1
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    ans+=1
        ans += len(stack)
        return ans
            