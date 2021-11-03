class Solution:
    def __init__(self) -> None:
        self.nums = []
    
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        help_index = self.findPivot(0,len(nums)-1)
        print(help_index)
        if help_index == -1:
            return 0
        if len(nums) > 1:  
            return help_index
        else:
            return 0

    def findPivot(self, low, high):
        if high < low:
            if self.nums[0] < self.nums[(len(self.nums) - 1)]:
                return (len(self.nums) - 1)
            else:
                return 0
        if high == low:
            return low
        mid = int((low + high)/2)
        if mid < high and self.nums[mid] > self.nums[mid + 1]:
            if mid != 0:
                if self.nums[mid] > self.nums[mid - 1]:
                    return mid
        if mid > low and self.nums[mid] > self.nums[mid - 1]:
            if mid + 1 <= (len(self.nums) - 1):
                if self.nums[mid] > self.nums[mid + 1]:
                    return mid
            if mid == (len(self.nums) - 1):
                    return mid
        if self.nums[low] >= self.nums[mid]:
            return self.findPivot(low, mid-1)
        return self.findPivot(mid, high)