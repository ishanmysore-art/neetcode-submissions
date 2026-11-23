class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        cache = [-1] * (n+1)
        cache[0], cache[1], cache[2] = 0, 1, 1

        def dp(i):
            cache[i] = cache[i-3] + cache[i-2] + cache[i-1]
            if i == n:
                return cache[i]
            return dp(i+1)

        return dp(3)
