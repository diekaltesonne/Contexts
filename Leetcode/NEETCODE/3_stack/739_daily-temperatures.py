# NOT SOLVE FOR MYSELF
class Solution:
    def _dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures 
        i = len(t) -1
        ans = [0] * len(t)
        stack = [[0,-1]]
        stack_1 = []
        while i >=0:
            ans[i] = 1000
            while stack[-1][0] > t[i]:  
                x = stack.pop()
                if ans[i] > x[1] - i:
                    ans[i] = (x[1] - i)
                stack_1.append(x)
           
            if len(stack_1) == 0:
                ans[i] = 0
                stack.append([t[i],i])    
            else:
                stack.append([t[i],i])
                stack_1.reverse()
                stack = stack + stack_1 
                stack_1.clear()
            i = i - 1
        return ans

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        stack = []
        size = len(t)
        ans = [0] * size

        for i in range(size):
            if not stack or t[i] <= stack[-1][0]:
                stack.append((t[i],i))
                continue
            
            while stack and t[i] > stack[-1][0]:
                temp, idx = stack.pop()
                ans[idx] = abs(i - idx)

            stack.append((t[i],i))
        
        return ans 






















