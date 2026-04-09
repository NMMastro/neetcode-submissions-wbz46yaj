class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Find upper bound to k
        low = 1
        high = piles[0]
        k = -1

        for p in piles:
            high = max(high, p)

        # Binary Search to find ideal value of k

        while low <= high:
            k = math.floor((high + low) / 2)

            time = 0
            for p in piles:
                time += math.ceil(p / k)

            if time > h:
                low = k + 1
            elif high == k:
                return k
            else:
                high = k

        return None

            