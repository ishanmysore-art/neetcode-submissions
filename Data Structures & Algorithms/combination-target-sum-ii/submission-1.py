class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sublist = []
        candidates.sort()
        def dfs(i, left):
            # Base cases:
            if left == 0:
                res.append(sublist.copy())
                return
            if left < 0 or i >= len(candidates):
                return
            # Two recursive cases: we either include the element in the sum, or we skip the element and move onto the rest of the list.
            sublist.append(candidates[i])
            dfs(i+1, left - candidates[i])
            sublist.pop()
            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, left)
        dfs(0, target)
        return res
