class Solution:
    def __init__(self) -> None:
        self.nums = []

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
        return self.findPivot(mid + 1, high)

    def _search(self,l,r,x):
        if len(self.nums) == 0 and x == 0:
            return -1
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if self.nums[mid] == x:
                return mid
            elif self.nums[mid] > x:
                return self._search(l, mid-1, x)
            # Else the element can only be present
            # in right subarray
            else:
                return self._search(mid + 1, r, x)
        else:
            
            return -1

    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        help_index = self.findPivot(0,len(nums)-1)
        print(help_index)
        if help_index == -1:
            return self._search(0,len(nums)-1,target)
        
        if help_index == len(nums)-1:
            return self._search(0,len(nums)-1,target)
        
        if self.nums[help_index] == target:
            return help_index
        
        if target == nums[-1]:
            return len(nums)-1
        
        if target > nums[-1]:
            return self._search(0,help_index,target)
        else:
            return self._search(help_index+1,len(nums)-1,target)

