class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0
        max_area = 0
        ma = [0]

        def dfs(i:int, j:int, ma:int ):
            grid[i][j] = -1
            ma[0] += 1 
            if(i < n - 1 and grid[i+1][j] == 1):
                dfs(i + 1,j,ma)
            if(i > 0 and grid[i-1][j] == 1):
                dfs(i - 1,j,ma)
            if(j < m - 1 and grid[i][j+1] == 1):
                dfs(i,j + 1,ma)
            if(j > 0 and grid[i][j - 1] == 1):
                dfs(i,j - 1,ma)
            
        for k in range(n):
            for l in range(m):
                #print(grid[k][l])
                if grid[k][l] == 1:
                    num_islands += 1
                    dfs(k,l,ma)
                    if ma[0] > max_area:
                        max_area = ma[0]
                    ma[0] = 0

        return max_area