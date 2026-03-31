class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort list
        # iterate thru array
        # large ptr and small ptr
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left_ptr = i + 1
            right_ptr = len(nums) - 1

            while left_ptr < right_ptr:
                left = nums[left_ptr]
                right = nums[right_ptr]
                curr = nums[i]
                total = left + right + curr
                if total < 0:
                    left_ptr += 1
                elif total > 0:
                    right_ptr -= 1
                elif total == 0:
                    res.append([left, curr, right])
                    while left_ptr < right_ptr and nums[left_ptr] == left:
                        left_ptr += 1
                    while left_ptr < right_ptr and nums[right_ptr] == right:
                        right -= 1
        return res