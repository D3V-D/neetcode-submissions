class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIdxMap = {}

        for i in range(len(nums)):
            lookup = target - nums[i]
            if lookup in valIdxMap:
                return [valIdxMap[lookup], i]
            valIdxMap[nums[i]] = i

