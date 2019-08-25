'''

A. Team
https://codeforces.com/problemset/problem/231/A

'''

n = int(input())

ctr = 0

for i in range(n):
    k = input()
    if k.count('1') > 1:
        ctr += 1
print(ctr)