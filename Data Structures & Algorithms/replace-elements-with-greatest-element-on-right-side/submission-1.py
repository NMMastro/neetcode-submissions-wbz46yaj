class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_element = arr[-1]
        arr[-1] = -1

        i = len(arr) - 2
        while i >= 0:
            old_greatest = greatest_element
            greatest_element = max(greatest_element, arr[i])
            arr[i] = old_greatest
            i -= 1
        
        return arr
            


        