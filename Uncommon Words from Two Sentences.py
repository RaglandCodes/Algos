'''

LeetCode 884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/

'''
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        sentances = A.split() + B.split()
        
        a = []
        for word in sentances:
            if sentances.count(word) == 1:
                a += [word]
        
        return a
        