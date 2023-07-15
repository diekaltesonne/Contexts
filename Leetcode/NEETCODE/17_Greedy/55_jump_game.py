class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

a = Solution()
print(a.canJump([2,3,1,1,4]))