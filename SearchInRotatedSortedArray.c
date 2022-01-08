/*

    LeetCode 33. Search in Rotated Sorted Array
    https://leetcode.com/problems/search-in-rotated-sorted-array/
*/

int find_pivot(int* nums, int left, int right){
    if (nums[left] < nums[right]){
        return -1;
    }
    
    int mid = left + (right-left)/2;
    if (mid == left){
        if(right>=1 && nums[left+1] < nums[mid])
            return left+1;   
        return left;
    }
    
    if (nums[mid-1] > nums[mid]){
        return mid;
    }
    
    if (nums[left] < nums[mid]){
        return find_pivot(nums, mid, right);
    }
    
    return find_pivot(nums, left, mid);
    
}

int binary_search(int* nums, int left, int right, int target){
    if (left>right)
        return -1;
    
    int mid = left + (right-left)/2;
    
    if (nums[mid] == target)
        return mid;
    
    if (nums[mid] < target)
        return binary_search(nums, mid+1, right, target);
    
    return binary_search(nums, left, mid-1, target);
}

int search(int* nums, int numsSize, int target){
    int pivot_idx = find_pivot(nums, 0, numsSize-1),
        from_left,
        from_right;
    
    if (pivot_idx > 0){
        from_left = binary_search(nums, 0, pivot_idx, target);
        from_right = binary_search(nums, pivot_idx, numsSize-1, target);  
        int ans = from_left;

        if (ans == -1)
            ans = from_right;

        return ans;
    }
    
    return binary_search(nums, 0, numsSize-1, target);
    
}