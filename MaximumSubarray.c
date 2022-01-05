/*

LeetCode 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

*/

int maxSubArray(int* nums, int numsSize){
    int max = nums[0];
    int max_now = nums[0];
    
    for(int i=1; i<numsSize; i++){
        if( max_now+nums[i] < nums[i] )
            max_now = nums[i];
        else
            max_now += nums[i];
        
        if( max_now > max )
            max = max_now;
        
    }
    
    return max;   
}