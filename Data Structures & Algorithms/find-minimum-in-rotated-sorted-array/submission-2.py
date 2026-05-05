class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        l = 0
        h = len(nums) - 1

        max = 0
        while l <= h:
            mid = math.floor((l + h) / 2)
            print(nums[mid])
            prev_num = mid - 1 if mid != 0 else len(nums) - 1

            # handles the case where it is correct
            if nums[mid] < nums[prev_num]:
                return nums[mid]

            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid - 1

        



        # idea: record the rightmost value

        # Perform BS

        # If the current value is less the value directly to it's left (modulo by size), then return that
        # If the current value is greater than the rightmost than it's the minimum
        # If the current value is less than the rightmost than it's the maximum

        # BS where the left element is reset 
        
        
        # 7 8 9 1 2 3 4 5 6





