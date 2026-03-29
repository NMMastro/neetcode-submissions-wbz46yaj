class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):      
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                start = stack.pop()
                res[start] = i - start

            stack.append(i)
        
        return res

            