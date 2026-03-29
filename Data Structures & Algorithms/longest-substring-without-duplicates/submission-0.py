class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        MaxLen = 0

        L = 0
        for R in range(len(s)):
            if not s[R] in letters:
                letters.add(s[R])
                MaxLen = max(MaxLen, len(letters))
            else:
                while s[L] != s[R]:
                    letters.remove(s[L])    
                    L += 1
                L += 1   

        return MaxLen

