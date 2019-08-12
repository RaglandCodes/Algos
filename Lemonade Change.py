'''

LeetCode 860. Lemonade Change
https://leetcode.com/problems/lemonade-change/

'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
            
            if bill > 5:
                if bill == 10:
                    if fives > 0:
                        fives -= 1
                    else:
                        return False
                else:
                    if fives>0 and tens>0 :
                        fives -= 1
                        tens -= 1
                    elif fives > 2:
                        fives -= 3
                    else:
                        return False
        
        return True
                    