'''

LeetCode 941. Valid Mountain Array
https://leetcode.com/problems/valid-mountain-array/

'''
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3:
            return False
        
        if (A[1] <= A[0]):
            return False

        current_subarray = "increasing"
        
        for i in range(0, length-1):
            if A[i+1]  == A[i]:
                    return False
                
            if current_subarray == 'increasing' and A[i+1] < A[i]:
                current_subarray = "decreasing"
            
            elif current_subarray == "decreasing" and A[i+1] > A[i]:
                return False
                
            
        if current_subarray == "increasing":
            return False
        
        return True
        