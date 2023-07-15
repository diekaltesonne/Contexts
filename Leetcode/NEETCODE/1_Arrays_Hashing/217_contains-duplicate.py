class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        count = -1
        for i in nums:
            if i in check:
                return True
            else:
                check[i] = 0
        print(check)
        return False