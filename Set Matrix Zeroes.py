'''

LeetCode 73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/

'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_row = len(matrix)
        n_col = len(matrix[0])
        rows_to_zero = [False] * n_row
        cols_to_zero = [False] * n_col
        zero_row = [0] * n_col
        
        for i in range(n_row):
            for j in range(n_col):
                if matrix[i][j] == 0:
                    rows_to_zero[i] = True
                    cols_to_zero[j] = True
                 
        def set_zero_row(z):
            matrix[z] = zero_row
            
        def set_zero_col(z):
            for i in range(n_row):
                matrix[i][z] = 0
                
        print(rows_to_zero)
        print(cols_to_zero)
        
        for z in range(n_row):
            if rows_to_zero[z]:
                set_zero_row(z)
        
        for z in range(n_col):
            if cols_to_zero[z]:
                set_zero_col(z)
            
            