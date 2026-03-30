class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        maxLen = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                count = 1
                val = x
                while val + 1 in nums_set:
                    val += 1
                    count += 1
                maxLen = count if count > maxLen else maxLen

        return maxLen
