class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        # dp = [[0 for i in range(n)] for j in range(m)]
        prev = [0 for i in range(n)] 
        
        for i in range(m):
            temp = [0 for i in range(n)] 
            for j in range(n):
                # print (dp)
                if i == 0 and j == 0 : temp[j] = grid[i][j]
                
                else:
                    up = grid[i][j]
                    if i>0: up += prev[j]
                    else: up += 9999
                    
                    left = grid[i][j]
                    if j>0: left += temp[j-1]
                    else: left += 9999
                    
                    temp[j] = min(left,up)
            prev =  temp
        
        return prev[-1]
        