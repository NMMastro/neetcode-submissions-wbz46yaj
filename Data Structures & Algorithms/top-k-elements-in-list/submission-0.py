class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # construct a dictionary to store {value: count}
        value_count_dict = {}

        for num in nums:
            if num in value_count_dict:
                value_count_dict[num] += 1
            else:
                value_count_dict[num] = 1
        
        # aline value_count_dict to count_values array
        count_values = [[] for _ in range(len(nums) + 1)]

        for index, (value, count) in enumerate(value_count_dict.items()):
            count_values[count].append(value)

        
        # return top k elements
        top_k = []
        items_added = 0
        for arr in reversed(count_values):
            if len(arr) != 0:
                for num in arr:
                    top_k.append(num)
                    items_added += 1
                if items_added >= k:
                    break
        return top_k