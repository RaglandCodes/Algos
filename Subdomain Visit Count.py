'''

LeetCode 811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/

'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        d = {}
        a = []
        
        for domain in cpdomains:
            s = domain.split()
            count = int(s[0])
            site = s[1]
            
            subDomains = site.split('.')
            sdList = []     # sd means sub domain
            for subDomain in subDomains[::-1]:
                if sdList == []:
                    sdList += [subDomain]
                else:
                    sdList += [subDomain + "." +sdList[-1]]
            
            for sd in sdList:
                if sd in d:
                    d[sd] += count
                else:
                    d[sd] = count
            
        for k, v in d.items():
            a += [str(v) +" "+ k]
            
        return a
        
        
            
        
        