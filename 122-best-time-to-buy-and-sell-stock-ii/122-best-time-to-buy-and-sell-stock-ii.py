class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        net = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                net += prices[i+1]-prices[i]
        return net