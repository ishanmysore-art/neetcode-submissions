class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sublist = []
        def dfs(i):
            if len(sublist) == k:
                res.append(sublist.copy())
                return
            if i <= n:
                sublist.append(i)
                dfs(i+1)
                sublist.pop()
                dfs(i+1)
        dfs(1)
        return res
