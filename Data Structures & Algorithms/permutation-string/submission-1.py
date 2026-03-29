class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Built s1 frequency dictionary
        s1_freq = {}

        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        # Make window that looks 
        start = 0
        end = 0
        window_freq = {}
        for end in range(len(s2)):
            window_freq[s2[end]] = window_freq.get(s2[end], 0) + 1

            if s2[end] not in s1_freq:
                start = end + 1
                window_freq = {}

            elif s1_freq[s2[end]] < window_freq[s2[end]]:             
                while s1_freq[s2[end]] < window_freq[s2[end]]:
                    window_freq[s2[start]] -= 1
                    start += 1
            
            elif end - start + 1 == len(s1):
                return True

        return False


        




        window_arr = [0] * 26