class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVal = 0

        while left < right:
            leftVal = heights[left]
            rightVal = heights[right]
            minV = leftVal if rightVal > leftVal else rightVal
            area = minV * (right - left)
            maxVal = area if area > maxVal else maxVal

            if leftVal < rightVal:
                left += 1
            else:
                right -= 1
        return maxVal