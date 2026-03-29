class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_run = 0

        for n in numset:
            if not (n - 1) in numset:
                run_length = 1
                while (n + run_length) in numset:
                    run_length += 1
                longest_run = max(longest_run, run_length)
        
        return longest_run
