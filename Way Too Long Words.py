'''

Codeforces 71 A Way Too Long Words
https://codeforces.com/problemset/problem/71/A

'''
n = int(input())

for i in range(n):
    w = input()
    len_w = len(w)
    if len_w > 10:
        w = w[0] + str(len_w - 2) + w[-1]

    print(w)
