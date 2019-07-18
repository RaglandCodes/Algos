'''

LeetCode 989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/

'''

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        A = int("".join(str(i) for i in A))
        return [int(i) for i in list(str(A + K))]   
