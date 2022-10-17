#User function Template for python3

class Solution:
    def dfs(self,node,adjL,visited):
        visited[node] = True
        for e in adjL[node]:
            if not visited[e]:
                self.dfs(e,adjL,visited)
        
    def numProvinces(self, adj, V):
        
        adjL = [[] for e in range(V)]
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i!=j:
                    adjL[i].append(j)
                    adjL[j].append(i)
        # print(adjL)         
        
        # code here 
        count = 0
        visited = [False for e in range(V)]
        for i in range(V):
            if not visited[i]:
                count = count + 1
                self.dfs(i,adjL,visited)
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends