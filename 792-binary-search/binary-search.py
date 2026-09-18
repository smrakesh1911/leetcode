class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                #RIGHT
                l =mid+1
            else:
                #left
                r =mid-1
        return -1
