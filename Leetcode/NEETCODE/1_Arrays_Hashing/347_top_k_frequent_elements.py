class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        table = {}
        mfe = [[0, 0] for i in range(k)]
        print(mfe)
        for i, v  in enumerate(nums):
            if v in table:
                table[v] += 1
            else:
                table[v] = 0
            # for j in range(k):    
            #     if table[v] > mfe[j][1] and (table[v] < mfe[j - 1][1]):
            #         mfe[j][1] = table[v]
            #         mfe[j][0] = v
        return sorted(table, key=lambda k: (-table[k], k))[:k]