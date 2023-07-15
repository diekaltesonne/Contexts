class Solution:
    def __init__(self) -> None:
        self.nums = []
    
    def findMin(self, nums: List[int]) -> int:
        self.nums = nums
        help_index = self.findPivot(0,len(nums)-1)
        print(nums[help_index])
        if help_index == -1:
            return nums[0]
        if len(nums) > 1:  
            if nums[help_index + 1] < nums[0]:
                return nums[help_index + 1]
            else:
                return nums[0]
        else:
            return nums[0]

    def findPivot(self, low, high):
        if high < low:
            return -1
        if high == low:
            return low
        mid = int((low + high)/2)
        if mid < high and self.nums[mid] > self.nums[mid + 1]:
            return mid
        if mid > low and self.nums[mid] < self.nums[mid - 1]:
            return (mid-1)
        if self.nums[low] >= self.nums[mid]:
            return self.findPivot(low, mid-1)
        return self.findPivot(mid, high)