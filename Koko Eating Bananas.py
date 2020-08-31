'''

LeetCode 875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/submissions/

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def can_koko_eat(speed):
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p/float(speed))
                if time_taken > H:
                    return False
            return True

    
        low = 1
        high = max(piles) +1 
        
        while low < high:
            mid = low + ((high - low) // 2)
            if can_koko_eat(mid):
                high = mid
            else:
                low = mid+1
        
        
        return low