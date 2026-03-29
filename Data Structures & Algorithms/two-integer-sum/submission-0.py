class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Need to know the first index and it's number
        # Hash (number, index)

        old_nums = {}

        for i in range(len(nums)):
            if (target - nums[i]) in old_nums:
                return [old_nums[target-nums[i]], i]
            else:
                old_nums[nums[i]] = i

        return [0, 0]