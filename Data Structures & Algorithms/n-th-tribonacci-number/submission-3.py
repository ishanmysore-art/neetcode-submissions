class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        cache = [0] * (n+1)
        cache[1], cache[2] = 1, 1

        for i in range(3, n+1):
            cache[i] = cache[i-3] + cache[i-2] + cache[i-1]

        return cache[n]
