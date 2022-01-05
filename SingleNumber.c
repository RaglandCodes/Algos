/*

    LeetCode 136. Single Number
    https://leetcode.com/problems/single-number

*/

int singleNumber(int* nums, int numsSize){
    int ans = nums[0], 
        i=1;
    
     while(i<numsSize)
        ans ^= nums[i++];
        
    return ans;
    
}