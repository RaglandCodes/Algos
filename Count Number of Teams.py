'''

LeetCode 1395. Count Number of Teams
https://leetcode.com/problems/count-number-of-teams/

How to append by value
https://stackoverflow.com/questions/8744113/python-list-by-value-not-by-reference

This is a brute force solution
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = []
        l = len(rating)
        
        for i in range(l):
            saved = []
            for t in teams:
                len_t = len(t)
                
                if len_t == 3:
                    continue
                if len_t == 2:
                    if t[1] > t[0] and rating[i] > t[1]:
                        saved.append(t[:])
                        t.append(rating[i])
                    elif t[1] < t[0] and rating[i] < t[1]:
                        saved.append(t[:])
                        t.append(rating[i])
                if len_t == 1:
                    saved.append(t[:])
                    t.append(rating[i])
            
            teams.append([rating[i]])
            teams += saved
            
        return len(list(filter(lambda x: len(x) == 3, teams)))
        
        