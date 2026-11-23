class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cache = [-1] * n

        # Instead of passing a smaller tuple cost[1:], keep cost untouched and pass an integer index i  representing where you currently are on the stairs:

        def dp(i):
            if i >= n:
                return 0
            if i == n-1:
                return cost[i]
            if cache[i] != -1:
                return cache[i]

            skip1 = cost[i] + dp(i+1)
            skip2 = cost[i] + dp(i+2)
            
            cache[i] = min(skip1, skip2)
            return cache[i]

        start0 = dp(0)
        start1 = dp(1)
        return min(start0, start1)