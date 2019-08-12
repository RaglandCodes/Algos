'''
LeetCode 1005. Maximize Sum Of Array After K Negations
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
'''
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        for i in range(K):
            m =  min(A)
            A[A.index(m)] = 0 - m
        
        return sum(A)
    
    
        
#         for i in range(K):
#             A = sorted(A)
            
#             change = A[0]
#             A = A[1:] + [0-change]
            
#         return sum(A)
    
            
