class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        i = 0
        while i < len(nums) - 2:
            cur_num = nums[i]

            target = 0 - cur_num
            left = i + 1
            right = len(nums) - 1

            while left < right:
                left_num = nums[left]
                right_num = nums[right]

                if left_num + right_num == target:
                    results.append([cur_num, left_num, right_num])
                    while nums[left] == left_num and left < right: left += 1

                elif left_num + right_num < target:
                    while nums[left] == left_num and left < right: left += 1

                else:
                    while nums[right] == right_num and left < right: right -= 1
            
            while nums[i] == cur_num and i < len(nums) - 2: i += 1

        return results




