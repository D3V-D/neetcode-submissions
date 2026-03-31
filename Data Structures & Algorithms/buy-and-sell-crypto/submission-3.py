class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0
        
        for x in prices:
            if x < minVal:
                minVal = x
            else:
                if x - minVal > maxProfit:
                    maxProfit = x - minVal
        
        return maxProfit
