#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def bfs(self,row,col,visited,grid):
        n = len(grid)
        m = len(grid[0])
        
        visited[row][col]=1
        queue = []
        queue.append((row,col))
        
        while queue:
            node = queue.pop(0)
            row = node[0]
            col = node[1]
            
            for drow in range(-1,2):
                for dcol in range(-1,2):
                    nrow = row + drow
                    ncol = col + dcol
                    if nrow >=0 and nrow < n and ncol >= 0 and ncol < m:
                        if grid[nrow][ncol] == 1 and not visited[nrow][ncol]:
                            visited[nrow][ncol] = 1
                            queue.append((nrow,ncol))
        
    def numIslands(self,grid):
        #code here
        
        n = len(grid)
        m = len(grid[0])
        cnt =0
        visited = [[False for j in range(m)] for i in range(n)]
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and not visited[row][col]:
                    cnt += 1
                    self.bfs(row,col,visited,grid)
        return cnt
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends