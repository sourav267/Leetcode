class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		n = len(grid)
		m = len(grid[0])
		cntFresh = 0
		queue = []
		visited = [[False for j in range(m)] for i in range(n)]
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==2:
		            queue.append([[i,j],0])
		            visited[i][j] = True
		        if grid[i][j] == 1:
		            cntFresh += 1
        tm = 0
        drow = [-1,0,+1,0]
        dcol = [0,1,0,-1]
        cnt = 0
        while queue:
            e = queue.pop(0)
            r = e[0][0]
            c = e[0][1]
            t = e[1]
            tm = max(tm,t)
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if nrow >= 0 and nrow <n and ncol >= 0 and ncol<m:
                    if  not visited[nrow][ncol] and grid[nrow][ncol] == 1:
                        queue.append([[nrow,ncol],t+1])
                        visited[nrow][ncol] = True
                        cnt += 1
        
        if cnt != cntFresh:
            return -1
        
        return tm
                        
            
            
            
		            


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends