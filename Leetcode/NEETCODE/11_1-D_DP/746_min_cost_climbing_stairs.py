class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int :
        mem = [0] * (len(cost) + 1)
        mem[0] = cost[0]
        mem[1] = cost[1]
        cost = cost + [0]
        for i in range(2,len(cost)):
            mem[i] = min(mem[i-1], mem[i-2]) + cost[i]
        return mem[-1]

a = Solution()
cost = [10, 15, 20]
print(a.minCostClimbingStairs(a.minCostClimbingStairs(cost)))