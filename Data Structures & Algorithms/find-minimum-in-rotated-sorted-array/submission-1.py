class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # start in middle
        # look for point where a value to the right is 
        # smaller than value to the left
        # THIS is our rotation point
        # AND... the value on the right must be the smallest

        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l != r:
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[l] > nums[mid]:
                # move to left half
                r = mid
                mid = (l + r) // 2
            elif nums[r] < nums[mid]:
                # move to right half
                l = mid
                mid = (l + r) // 2
            else:
                # sorted?
                return nums[0]
        return nums[mid]
