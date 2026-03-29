class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        # Prefixs
        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix = prefix * nums[i]

        # Postfixs
        postfix = 1
        for i in reversed(range(len(nums))):
            products[i] *= postfix
            postfix *= nums[i]

        return products
        


