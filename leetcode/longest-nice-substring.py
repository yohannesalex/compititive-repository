class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest_substring = ""
        stack = [s]
        while stack:
            word = stack.pop()
            if not word:
                continue
            char_set = set(list(word))
            for i, char in enumerate(word):
                if char.swapcase() not in char_set:
                    stack.append(word[i+1:])
                    stack.append(word[:i])
                    break
            else:
                longest_substring = max(longest_substring, word, key=len)
        return longest_substring