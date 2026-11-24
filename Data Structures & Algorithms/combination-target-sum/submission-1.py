class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sublist = []

        def dfs(i, left):
            if left == 0:
                res.append(sublist.copy())
                return
            
            if i >= len(nums) or left < 0:
                return

            if nums[i] <= left:
                sublist.append(nums[i])
                dfs(i, left-nums[i])
                sublist.pop()
                
            dfs(i+1, left)
        
        dfs(0, target)
        return res
