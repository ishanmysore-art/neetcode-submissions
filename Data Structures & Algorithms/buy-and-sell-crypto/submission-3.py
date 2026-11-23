class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 1
        curr_profit = 0
        while i < len(prices) and j < len(prices):
            if prices[j] < prices[i]:
                i = j
            else:
                max_profit = max(max_profit, prices[j] - prices[i])
            j += 1

        return max_profit