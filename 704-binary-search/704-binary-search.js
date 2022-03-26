/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    l = 0
    r = nums.length-1
    while(l<=r){
        mid = l + parseInt((r-l)/2)
        if (nums[mid] == target){
            return mid}
        else if(nums[mid] < target){
            l = mid + 1
        }
        else{
            r = mid - 1
        }
    }
    return -1 ;
};