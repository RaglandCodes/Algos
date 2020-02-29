'''

LeetCode 1338. Reduce Array Size to The Half
https://leetcode.com/problems/reduce-array-size-to-the-half/

The commented out code gives time limit exceeded

'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        target_length = 0
        d = {}
        
        for n in arr:
            target_length += 0.5
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        cset = [[k, v] for k, v in d.items()]
        cset.sort(key = lambda x: x[1], reverse = True)
        a = 0
        removed = 0
        
        for c in cset:
            a += 1
            removed += c[1]
            if removed >= target_length:
                return a
            
        return a
    
        '''
        target_length = len(arr)/2
        
        cset = [[s, arr.count(s)] for s in set(arr)]
        cset.sort(key = lambda x: x[1], reverse = True)
        a = 0
        removed = 0
        
        for c in cset:
            a += 1
            removed += c[1]
            if removed >= target_length:
                return a
            
            
            
        return a
        '''    