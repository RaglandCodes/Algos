'''
LeetCode Group Anagrams

Answer from here https://leetcode.com/problems/group-anagrams/discuss/597965/Clean-Python3-Solution

With defaultict, no need to check if value exists. 

the keys must be immutable and so we need to make it a tuple 
https://qr.ae/pNrqJK

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for word in strs:
            letters = tuple(sorted([c for c in word]))
            d[letters].append(word)

        return list(d.values())