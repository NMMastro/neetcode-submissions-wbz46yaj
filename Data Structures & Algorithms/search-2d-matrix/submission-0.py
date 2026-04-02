class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Use 1d coordinates
        # Top left box will be index 0
        # Bottom right box will be index m * n - 1

        # BS where we get the value by matrix[floor(index / m)][index % m]

        # If not found return false

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            middle = math.floor((right + left) / 2)
            current_value = matrix[math.floor(middle / n)][middle % n]

            if current_value == target:
                return True
            elif current_value < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False




