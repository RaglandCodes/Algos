'''

LeetCode 950. Reveal Cards In Increasing Order
https://leetcode.com/problems/reveal-cards-in-increasing-order/submissions/

'''
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        l = len(deck)
        a = [0 for d in deck]
        ptr = 0
        added = 0
        skip = False
        while added < l:
            for i in range(l):
                if a[i] == 0:
                    if skip:
                        skip = False
                    else:
                        a[i] = deck[ptr]
                        ptr += 1
                        added += 1
                        skip = True
                        
        return a
    