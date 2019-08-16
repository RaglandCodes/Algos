'''

LeetCode 500. Keyboard Row
https://leetcode.com/problems/keyboard-row/

'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        
        a = []
        
        for word in words:
            
            if len(word) == 1:
                a += [word]
                continue
                
            w = word
            word = word.lower()
            
            if word[0] in row1:
                currentRow = 1
            elif word[0] in row2:
                currentRow = 2
            else:
                currentRow = 3
            
            for i in range(1, len(word)):
                if currentRow == 1:
                    if word[i] not in row1:
                        break
                        
                elif currentRow == 2:
                    if word[i] not in row2:
                        break
                        
                elif currentRow == 3:
                    if word[i] not in row3:
                        break
                
                if i+1 == len(word):
                    a += [w]
        
        return a
