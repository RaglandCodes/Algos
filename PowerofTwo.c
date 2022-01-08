/*

LeetCode 231. Power of Two
https://leetcode.com/problems/power-of-two/

Answer from http://graphics.stanford.edu/~seander/bithacks.html#DetermineIfPowerOf2

Based on the fact that power of 2 numbers are a complement of their previous number
*/

bool isPowerOfTwo(long int n){
    return n && !(n & n-1);
}