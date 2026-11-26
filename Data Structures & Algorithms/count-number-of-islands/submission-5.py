class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # keep a set of the "squares" we have visited: probably a set of (x, y) coordinates in a set
        visited = set()
        m, n = len(grid), len(grid[0])

        # graph traversal problem
        def dfs(x, y):
            # check base cases: if we are out of bounds, or if we reach a 0, or if we've visited the square already, return false
            # mark this square as visited
            # check up, down, left, and right recursively
            # return true perhaps??
            if (x >= m or y >= n or x < 0 or y < 0):
                return False
            if grid[x][y] == "0" or (x, y) in visited:
                return False
            visited.add((x, y))
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return True

        # loop through all coordinates, do dfs on each one
        # if dfs returns true for a coordinate, add 1 to res
        return sum(dfs(x, y) for x in range(m) for y in range(n))