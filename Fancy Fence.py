'''

Codeforces
A. Fancy Fence
https://codeforces.com/problemset/problem/270/A

'''
n = int(input())
q = []

def check(a):
    return 360 % (180 - a) == 0

for i in range(n):
    q = int(input())

    if 360 % (180 - q) == 0:
        print("YES")
    else:
        print("NO")
    