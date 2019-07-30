'''
LeetCode 929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        for i, email in enumerate(emails):
            
            at_index = email.index('@')
            local_name = email[:at_index]
            domain_name = email[at_index:]
            
            local_name = local_name.replace(".", "")
            
            if('+' in local_name):
                local_name = local_name[:local_name.index('+')]
            
            emails[i] = local_name+domain_name
        
        return(len(set(emails)))
                        