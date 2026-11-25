class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        visited = [False] * len(nums)
        def dfs(i):
            # Base cases:
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    perm.append(nums[i])
                    dfs(i)
                    visited[i] = False
                    perm.pop()
        
        dfs(0)
        return res