#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited = [0 for i in range(V)]
        visited[0] = 1
        queue=[]
        queue.append(0)
        bfs = []
        while queue:
            node = queue.pop(0)
            bfs.append(node)
            for e in adj[node]:
                if visited[e] == 0:
                    visited[e] = 1
                    queue.append(e)
        return bfs
            
            


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends