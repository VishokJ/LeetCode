class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        maxProfit = 0
        for n in prices:
            if n < minVal: minVal = n
            elif n - minVal > maxProfit: maxProfit = n - minVal
        return maxProfit