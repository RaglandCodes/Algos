'''

LeetCode 1347. Minimum Number of Steps to Make Two Strings Anagram
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

'''
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        a = 0
        for k in count_s:
            if k in count_t:
                if count_s[k] > count_t[k]:
                    a += (count_s[k] - count_t[k])
            else:
                a += count_s[k]
        return a
        