import copy
class Solution:
    def pacificAtlantic(self, heights):
        heights_1 = copy.deepcopy(heights)
        n = int(len(heights))
        m = int(len(heights[0]))
        ans = []
        check = [0,0]

        def dfs(i:int, j:int, check):
            if check[0] == 1 and check[1] == 1:
                return
            
            if((i==0)) or (j==0):
                check[0] = 1
            if((i== n-1 )) or (j== m-1):
                check[1] = 1 
            
            heights_1[i][j] = -1 
            if(i < n - 1 and heights_1[i+1][j]<= heights_1[i][j] and heights_1[i+1][j]!= -1):
                dfs(i + 1,j,check)
            if(i > 0 and heights_1[i-1][j] <= heights_1[i][j] and heights_1[i-1][j]!= -1):
                dfs(i - 1,j,check)
            if(j < m - 1 and heights_1[i][j+1] <= heights_1[i][j] and heights_1[i][j+1]!= -1):
                dfs(i,j + 1,check)
            if(j > 0 and heights_1[i][j - 1] <= heights_1[i][j] and heights_1[i][j-1]!= -1):
                dfs(i,j - 1,check)


        for k in range(n):
            for l in range(m):
                dfs(k,l,check)
                print(check)
                if check[0] == 1 and check[1] == 1:
                    ans.append([k,l])
                heights_1 = copy.deepcopy(heights)
                check =[0,0]

        return ans
    
a = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(a.pacificAtlantic(heights))