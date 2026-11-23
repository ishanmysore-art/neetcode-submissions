class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        cost = tuple(cost)

        def dp(cost):
            if not cost:
                return 0
            if len(cost) == 1:
                return cost[0]
            if cost in cache:
                return cache[cost]

            skip1 = cost[0] + dp(cost[1:])
            skip2 = cost[0] + dp(cost[2:])
            
            cache[cost] = min(skip1, skip2)
            return cache[cost]

        start0 = dp(cost)
        start1 = dp(cost[1:])
        return min(start0, start1)