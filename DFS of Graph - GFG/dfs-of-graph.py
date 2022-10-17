#User function Template for python3

class Solution:
    
    def dfs(self,node,visited,adj,dfsList):
        visited[node]=True
        dfsList.append(node)
        # print(dfsList)
        for e in adj[node]:
            if not visited[e]:
                self.dfs(e,visited,adj,dfsList)
                
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False for e in range(V)]
        dfsList = []
        start = 0
        self.dfs(start,visited,adj,dfsList)
        return dfsList
        

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends