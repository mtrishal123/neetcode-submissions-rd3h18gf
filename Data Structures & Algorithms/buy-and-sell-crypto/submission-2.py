class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, profit = 0, 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                if profit < prices[right] - prices[left]:
                    profit = prices[right] - prices[left]
        return profit