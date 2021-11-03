class Solution:
    def __init__(self) -> None:
        self.nums = []

    
    def search(self,l,r,x):
        if len(self.nums) == 0 and x == 0:
            return [-1,-1]
        if r >= l:
            mid = l + (r - l) // 2
            # If element is present at the middle itself
            if self.nums[mid] == x:
                l = mid
                r = mid
                for i in range(mid,len(self.nums)):
                    if self.nums[i] == x:
                        r = i
                for i in range(mid,-1,-1):
                    if self.nums[i] == x:
                        l = i
                return [l,r]
            elif self.nums[mid] > x:
                return self.search(l, mid-1, x)
            # Else the element can only be present
            # in right subarray
            else:
                return self.search(mid + 1, r, x)
        else:
            # Element is not present in the array
            return [-1,-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        return self.search(0,len(nums)-1,target)
