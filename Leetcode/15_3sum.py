class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets_dict= {}
        if len(nums) == 1 or not nums:
            return []
        nums.sort()
        for i in range(len(nums) - 2):
            right = len(nums) - 1
            left = i + 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet.sort()
                    if triplet not in triplets_dict:
                        triplets_dict[triplet] = 1
                    left += 1 
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return list(triplets_dict.keys())
        