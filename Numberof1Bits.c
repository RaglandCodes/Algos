/*

LeetCode 191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Answer from http://graphics.stanford.edu/~seander/bithacks.html

*/
int hammingWeight(uint32_t n) {
    int ans = 0;
    for(ans=0; n; ans++)
        n &= n-1;

    return ans;
}