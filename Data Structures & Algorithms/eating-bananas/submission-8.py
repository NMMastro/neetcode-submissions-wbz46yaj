class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Find upper bound to k
        low = 1
        high = max(piles)
        res = high

        # Binary Search to find ideal value of k

        while low <= high:
            k = math.floor((high + low) / 2)

            time = 0
            for p in piles:
                time += math.ceil(p / k)

                if time > h:
                    break

            if time > h:
                low = k + 1
            else:
                res = k
                high = k - 1

        return res

            