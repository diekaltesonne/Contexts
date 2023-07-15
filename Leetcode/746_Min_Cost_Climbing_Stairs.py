class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [1, 2]
        min_cost = [0] * len(cost)
        l = 0
        for i in range(l,len(cost),1):
            min_cost[i] = 100000
            for j in range(i):
                if i >= steps[j]:
                    num_cost = min_cost[i - steps[j]] + 1
                if num_cost < min_cost[i]:
                    min_num_coins[i] = num_coins
        print(min_cost)
        return min_cost[-1]