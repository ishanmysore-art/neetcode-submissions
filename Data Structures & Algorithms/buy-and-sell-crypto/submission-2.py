class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 1
        curr_profit = 0
        while i < len(prices) and j < len(prices):
            if prices[j] < prices[i]:
                j += 1
            else:
                while j < len(prices):
                    max_profit = max(prices[j]-prices[i], max_profit)
                    j += 1
                j = i + 2
            i += 1

        return max_profit