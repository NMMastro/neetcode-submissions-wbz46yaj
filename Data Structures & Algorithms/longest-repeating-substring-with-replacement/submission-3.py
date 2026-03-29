class Solution:

    def max_count(self, frequency):
        max_freq = 1
        for char, freq in frequency.items():
            max_freq = max(max_freq, freq)
        return max_freq


    def characterReplacement(self, s: str, k: int) -> int:

        frequency = {}
        max_len = 1

        start = 0
        end = 0

        while end < len(s):
            frequency[s[end]] = frequency.get(s[end], 0) + 1

            window_size = end - start + 1
            if window_size - self.max_count(frequency) <= k:
                max_len = max(max_len, window_size)
            else:

                frequency[s[start]] -= 1
                start += 1
            end += 1

        
        return max_len