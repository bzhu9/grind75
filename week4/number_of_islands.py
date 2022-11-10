class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        d = [0, 1, 0, -1, 0]
        def dfs(grid, r, c):
            if len(grid) > r >= 0 <= c < len(grid[0]):
                if grid[r][c] != "1":
                    return
                grid[r][c] = 0
                for i in range(4):
                    dfs(grid, r + d[i], c + d[i + 1])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1
        return count
