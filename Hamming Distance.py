'''

LeetCode 461. Hamming Distance
https://leetcode.com/problems/hamming-distance/

'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return (bin(x^y)).count('1')
        