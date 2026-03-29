class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        letter_counts = {}

        for char in s:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
        
        for char in t:
            if not (char in letter_counts):
                return False
            else:
                letter_counts[char] -= 1
                if letter_counts[char] == 0:
                    letter_counts.pop(char)
        
        return True
                