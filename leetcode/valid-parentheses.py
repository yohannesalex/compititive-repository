class Solution:
    def isValid(self, s: str) -> bool:



        stack = []

        openings = {"(":')', "{":"}", "[":']'}

        for symbol in s:
           
            if symbol in openings:
               stack.append(symbol)
            else:
                if not stack:
                    return False
                #"]"
                if symbol != openings[stack[-1]]:
                    return False

                stack.pop()
        if stack:
            return False
        return True
