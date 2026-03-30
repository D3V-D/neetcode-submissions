class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxLen = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                count = 1
                while x + count in nums_set:
                    count += 1
                maxLen = count if count > maxLen else maxLen

        return maxLen
