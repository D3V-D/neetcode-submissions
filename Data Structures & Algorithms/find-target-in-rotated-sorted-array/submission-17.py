class Solution:
    def binary_search(self, start_idx, end_idx, nums, target):
        l = start_idx
        r = end_idx

        while (l <= r):
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l != r:
            if nums[mid] > nums[mid + 1]:
               # we have cut point
               break
            
            if nums[l] > nums[mid]:
                # move to left half
                r = mid
                mid = (l + r) // 2
            elif nums[r] < nums[mid]:
                # move to right half
                l = mid
                mid = (l + r) // 2
            else:
                # sorted
                mid = -1
                break
        
        if mid == -1:
            return self.binary_search(0, len(nums) - 1, nums, target)
        l_idx = self.binary_search(mid + 1, len(nums) - 1, nums, target)
        r_idx = self.binary_search(0, mid, nums, target)
        
        if r_idx != -1:
            return r_idx
        if l_idx != -1:
            return l_idx
        return -1
