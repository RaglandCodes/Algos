'''

LeetCode 856. Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/submissions/

'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        score = []  
        
        for b in S:
            if b == '(':
                score.append(0)
            else:
                if score[-1] == 0:
                    score[-1] = 1
                else:
                    for i in range(len(score) - 1, -1, -1):
                        if score[i] == 0:
                            break
                    score = score[0:i] + (2*[sum(score[i:])])
            
        return sum(score)
                    