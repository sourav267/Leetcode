class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        def f(i,j1,j2,grid,c,r,dp):

            if (j1<0 or j2<0 or j1>=c or j2>=c):
                return -1

            if i == r-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]

            if dp[i][j1][j2] != -1:return dp[i][j1][j2]

            maxi = -1
            for dj1 in range(-1, 2):
                for dj2 in range(-1,2):
                    value = 0
                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]

                    value += f(i+1,j1+dj1,j2+dj2,grid,c,r,dp)
                    maxi = max(maxi,value)

            dp[i][j1][j2] = maxi
            return maxi
        
        row = len(grid)
        col = len(grid[0])
        dp = [[[-1 for k in range(col)] for j in range(col)] for i in range(row)]
        ans = f(0,0,col-1,grid,col,row,dp)
        return ans
        # print(ans)