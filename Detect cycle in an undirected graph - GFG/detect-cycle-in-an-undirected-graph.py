

from typing import List
class Solution:
    def detectCycle(self,src,V,adj,visited):
        visited[src] = True
        queue = []
        queue.append([src,-1])
        while queue:
            temp = queue.pop(0)
            node = temp[0]
            parent = temp[1]
            
            for e in adj[node]:
                if not visited[e]:
                    visited[e] = True
                    queue.append([e,node])
                
                elif parent != e:
                    return True
        return False
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        visited = [False for e in range(V)]
        for v in range(V):
            if not visited[v]:
                if self.detectCycle(v,V,adj,visited):
                    return 1
        return 0
        

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
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends