class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        m, n = len(grid), len(grid[0])

        time, fresh = 0, 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row < 0 or row >= m) or (col < 0 or col >= n) or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return -1 if fresh else time
