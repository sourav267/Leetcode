/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function(nums, target) {
   
    
    const backtrack = (i,target,sum,n,nums) => {
        if(i==n){
            if(sum == target)return 1
            else return 0
        }
        const l = backtrack(i+1,target,sum+nums[i],n,nums)
        const r = backtrack(i+1,target,sum-nums[i],n,nums)
        return l+r
        
    }       
    
     return backtrack(0,target,0,nums.length,nums)
};