'''
Codeforces 363 B. Fence

https://codeforces.com/problemset/problem/363/B
'''
n, k = input().split()
n = int(n)
k = int(k)
f = list(map(int, input().split()))


def solve(n, k, f):
    a = 1
    ms = sum(f[:k])

    first = f[0]
    oldsum = ms
    for i in range(1, n - k +1):
        newsum = oldsum - first + f[i + k - 1]
        first = f[i]
        if newsum < ms:
            ms = newsum
            a = i + 1
        oldsum = newsum


    print(a)
        
           

solve(n, k, f)