/*
    LeetCode 169. Majority Element
    Using Boyer–Moore majority vote algorithm
*/

int majorityElement(int* nums, int numsSize){
    int ans = nums[0];
    unsigned int ctr = 1,
                 ptr = 1;
    
    while(ptr<numsSize){
        if (!ctr){
            ans = nums[ptr++];
            ++ctr;
            continue;
        }
        if(ans == nums[ptr++])
            ++ctr;
        else
            --ctr;
    }
    
    return ans;

}