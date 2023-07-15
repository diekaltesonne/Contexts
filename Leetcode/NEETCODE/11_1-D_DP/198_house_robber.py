class Solution:
    def rob(self, nums: int) -> int:
        if len(nums) == 1:
            return nums[0]
        mem = [0] * len(nums)
        mem[0] = nums[0]
        mem[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            mem[i] = max(mem[i - 1], mem[i - 2] + nums[i])
        return mem[-1]

            

        
    