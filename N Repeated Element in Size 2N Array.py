'''

LeetCode 961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/

'''
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counts = collections.Counter(A)
        
        #return counts.most_common(1)[0][0] # Alternate solution
        
        for k, v in counts.items():
            if v > 1:
                return k