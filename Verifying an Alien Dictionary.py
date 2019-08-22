'''

LeetCode 953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        
        for i, word in enumerate(words):
            word = list(word)
            for j, letter in enumerate(word):
                word[j] = alphabets[order.index(letter)]
            
            words[i] = "".join(word)
        
        return words == sorted(words)       
        