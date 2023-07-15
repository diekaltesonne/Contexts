class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in table.keys():          
                ans.append(i)
                ans.append(table[nums[i]])
            table[target - nums[i]] = i
        return ans 