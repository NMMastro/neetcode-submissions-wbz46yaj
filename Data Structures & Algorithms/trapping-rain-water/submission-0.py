class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        total = 0
        l_max = 0
        r_max = 0

        while l <= r:
            if l_max <= r_max:
                total += max(min(l_max, r_max) - height[l], 0)
                print(l, total)
                l_max = max(height[l], l_max)
                l += 1
            else:
                total += max(min(l_max, r_max) - height[r], 0)
                print(r, total)
                r_max = max(height[r], r_max)
                r -= 1
            
        return total