'''

Codeforces A. Elephant
https://codeforces.com/problemset/problem/617/A

'''

n = int(input())

ctr = 0

while n:
    if n-5 >= 0:
        n -= 5
        ctr += 1
        continue
    
    if n-4 >= 0:
        n -= 4
        ctr += 1
        continue
    
    if n-3 >= 0:
        n -= 3
        ctr += 1
        continue
    
    if n-2 >= 0:
        n -= 2
        ctr += 1
        continue
    
    if n-1 >= 0:
        n -= 1
        ctr += 1
        continue

print(ctr)
    
    