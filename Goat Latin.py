'''

LeetCode 824. Goat Latin
https://leetcode.com/problems/goat-latin/

'''
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split(" ")
        vowels = 'aeiouAEIOU'
        for i, word in enumerate(S):
            aaa = "".join(['a']*(i+1))
            if word[0] in vowels:
                S[i] += 'ma' + aaa
            else:
                S[i] = S[i][1:] + S[i][0] + 'ma' + aaa
            
        return " ".join(S)