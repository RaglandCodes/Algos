'''

Codeforces A. Stones on the Table

'''
n = int(input())
s = input()
a = 0

for i in range(0, n-1):
    if s[i] == s[i+1]:
        a+=1

print(a)





