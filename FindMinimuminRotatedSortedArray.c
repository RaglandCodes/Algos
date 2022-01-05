/*

LeetCode 153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Runtime is 0 ms (sometimes 4 ms)
https://leetcode.com/submissions/detail/607790581/

*/


// This functions finds the point where the rotate part ends
int firstEnd(int arr[], int left, int right){
    
    // Return -1 if  no rotation  is found in this part
    // (no rotation means all elemeents were in ascending order)
    if(left==right || (right==left+1 && arr[right]>arr[left]))
        return -1;
    
    int mid = left + (right-left)/2;
    
    if (arr[mid+1] < arr[mid])
        return mid;
    
    
    if(mid>0 && arr[mid-1] > arr[mid])
        return mid-1;
    
    int inLeftSide = firstEnd(arr, left, --mid);
    if (inLeftSide > -1)
        return inLeftSide;
    
    return firstEnd(arr, ++mid, right);   
}

int findMin(int* nums, int numsSize){
    return nums[firstEnd(nums, 0, numsSize-1) + 1];
}