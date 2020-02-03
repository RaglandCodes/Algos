'''

LeetCode 784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/

'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        a = [S]
        for i in range(len(S)):
            for j in range(len(a)):
                if a[j][i].isalpha():
                    a += [a[j][:i] + a[j][i].swapcase() + a[j][i+1:]]
        return a
                    
                
                
            
        
                
        