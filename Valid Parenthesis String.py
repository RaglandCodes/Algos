'''

LeetCode Valid Parenthesis String


The rems(p) function is to remove all the "()" I did that hoping to solve the Time Limit Exceeded problem.

But that function is not necessary to fix TLE.

the TLE was fixed by calling set after filter

'''
class Solution:
    def checkValidString(self, s: str) -> bool:

        def rems(p):
            old = p
            while True:
                rd = old.replace("()", "")
                if rd == old:
                    return rd
                old = rd
                
        def addToAll(arr, l):
            for i in range(0, l):
                arr[i] += 1
            return arr
        
        def rem(arr, l):
            for i in range(0, l):
                arr[i] -= 1
            
            return arr
        def star(arr, l):
            newp = []
            m = 0
            for n in arr:
                newp.append(n-1)
                newp.append(n)
                newp.append(n+1)
            return newp
        
        o = [0]
        l = 1
        
        #s = rems(s)
        for p in s:
            if p == "(":
                o = addToAll(o, l)
            elif p == ")":
                o  = rem(o, l)
                o = list(set(filter(lambda x: x >= 0, o)))
                l = len(o)
            elif p == "*":
                o = star(o, l)
                o = list(set(filter(lambda x: x >= 0, o)))
                l = len(o)
                
        return 0 in o