#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		def find_all_subset_sum(i,arr,n,sub_set_sum,ds):
            if i == n:
                ds.append(sub_set_sum)
                return
            else:
                find_all_subset_sum(i+1,arr,n,sub_set_sum+arr[i],ds)
                find_all_subset_sum(i+1,arr,n,sub_set_sum,ds)
        
        ds = []
        find_all_subset_sum(0,arr,N,0,ds)
        return ds
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends