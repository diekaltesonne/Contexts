class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        cache = set()
        for i in nums:
            if i not in cache:
                cache.add(i)
            else:
                cache.remove(i)
        answer = cache.pop()
        return answer