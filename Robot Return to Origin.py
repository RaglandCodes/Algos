'''
    LeetCode 657. Robot Return to Origin
    https://leetcode.com/problems/robot-return-to-origin/
'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
    
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
    
        return False
    
    ''' 
        I did the below one first. But the above one is shorter and faster
    
        
        vertical_movement = 0
        horizontal_movement = 0
        
        for l in moves:
            print(l)
            if l == 'U':
                vertical_movement += 1
            elif l == 'D':
                vertical_movement -= 1
            elif l == 'L':
                horizontal_movement -= 1
            else :
                horizontal_movement += 1
        
        if horizontal_movement == 0 and vertical_movement == 0:
            return True
        
        return False
    '''
	