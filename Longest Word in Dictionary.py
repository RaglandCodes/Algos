'''

LeetCode 720. Longest Word in Dictionary
https://leetcode.com/problems/longest-word-in-dictionary/submissions/

'''
from collections import deque
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=len)
        
        trie = {'val':"#", 'children':[]}
        
        def add_to_trie(w):
            l = len(w)
            if l == 1:
                trie['children'].append({'val':w, 'count':1, 'children':[]})
                return 1
            
            q = deque()
            q.append(trie)
            
            i = 0
            while True:
                node = q.popleft()
                for c in node['children']:
                    if c['val'] == w[i]:
                        i += 1
                        q.append(c)
                        break
                if not q:
                    if i+1 == l:
                        node['children'].append({'val':w[i], 'count':i+1, 'children':[]})
                        return i+1
                    return 0
                
        
        a_n = 0
        a_w = 0
        
        for word in words:
            c = add_to_trie(word)
            if c > a_n:
                a_n = c
                a_w = word
                continue
            if c == a_n:
                if word < a_w:
                    a_w = word
                    a_n = c
        
        return a_w
