class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        def dp(cost):
            if not cost:
                return 0
            if len(cost) == 1:
                return cost[0]
            if tuple(cost) in cache:
                return cache[tuple(cost)]

            skip1 = cost[0] + dp(cost[1:])
            skip2 = cost[0] + dp(cost[2:])
            
            cache[tuple(cost)] = min(skip1, skip2)
            return cache[tuple(cost)]

        start0 = dp(cost)
        start1 = dp(cost[1:])
        return min(start0, start1)