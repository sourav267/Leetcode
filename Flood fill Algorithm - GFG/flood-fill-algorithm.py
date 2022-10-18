class Solution:
    def dfs(self,r,c,ans,newColor,image,dRow,dCol,initColor):
        ans[r][c] = newColor
        
        n = len(image)
        m = len(image[0])
        
        for i in range(4):
            nrow = r + dRow[i]
            ncol = c + dCol[i]
            if nrow>=0 and nrow < n and ncol>=0 and ncol < m:
                if image[nrow][ncol] == initColor and ans[nrow][ncol] != newColor:
                    self.dfs(nrow,ncol,ans,newColor,image,dRow,dCol,initColor)
                
        
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		initColor = image[sr][sc]
		ans = image
		dRow = [-1,0,+1,0]
		dCol = [0, +1, 0, -1]
		
		self.dfs(sr,sc,ans,newColor,image,dRow,dCol,initColor)
		return ans
		



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends