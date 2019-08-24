'''

LeetCode 476. Number Complement
https://leetcode.com/problems/number-complement/

The logic is that num^x will give the answer.
where x is ones for the length of the binary represntation of 1

num^1s = ~num

It's mentioned in Cracking the Coding Interview [Book]

'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        return (int(('1'*(len(bin(num)) - 2)), 2) ^ num)