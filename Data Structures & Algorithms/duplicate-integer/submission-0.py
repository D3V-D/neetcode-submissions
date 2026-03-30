class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set()
        for x in nums:
            if x in s1:
                return True
            else:
                s1.add(x)
        return False