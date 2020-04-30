'''

Codeforces B. Borze
https://codeforces.com/problemset/problem/32/B

'''
import sys
input = sys.stdin.readline


borze = input() + "N"
a = ''

skip = False
for i, l in enumerate(borze):
    if skip:
        skip = False
        continue
    
    if l == '.':
        a += '0'
    elif l == '-':
        if borze[i+1] == '-':
            a += '2'
        else:
            a += '1'
        skip = True

print(a)

    
