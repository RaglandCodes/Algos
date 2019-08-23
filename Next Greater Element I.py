'''

LeetCode 496. Next Greater Element I 
https://leetcode.com/problems/next-greater-element-i/

'''
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = []
        len_nums_2 = len(nums2)
        
        for n1 in nums1:
            found = False
            for i in range(nums2.index(n1), len_nums_2):
                
                if nums2[i] > n1:
                    a += [nums2[i]]
                    found = True
                    break
                
            if not found:
                a += [-1]
        
        return a
    