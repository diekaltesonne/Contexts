#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0

        def dfs(i:int, j:int):
            grid[i][j] = "-1"
            if(i < n - 1 and grid[i+1][j] == "1"):
                dfs(i + 1,j)
            if(i > 0 and grid[i-1][j] == "1"):
                dfs(i - 1,j)
            if(j < m - 1 and grid[i][j+1] == "1"):
                dfs(i,j + 1)
            if(j > 0 and grid[i][j - 1] == "1"):
                dfs(i,j - 1)
            
        for k in range(n):
            for l in range(m):
                #print(grid[k][l])
                if grid[k][l] == "1":
                    num_islands += 1
                    dfs(k,l)

        return num_islands