'''

https://codeforces.com/problemset/problem/459/A
Codeforces A. Pashmak and Garden

'''
import sys
input = sys.stdin.readline

def intl():
    return(list(map(int,input().split())))
x1, y1, x2, y2 = intl()

delta = 0
mini = min(x1, y1, x2, y2)
if mini < 0:
    delta = 0 - mini
    x1 += delta
    x2 += delta
    
    y1 += delta
    y2 += delta

error = False
l = 0
x3 = x1
y3 = y1
x4 = x2
y4 = y2

if x1 == x2:
    l = abs(y1 - y2)
    x3 = x1 + l
    x4 = x2 + l
    y3 = y1
    y4 = y2

elif y1 == y2:
    l = abs(x1 - x2)
    x3 = x1
    x4 = x2
    y3 = y1 + l
    y4 = y2 + l

else:
    l = abs(x1 - x2)
    l2 = abs(y1 - y2)

    if not l == l2:
        error = True 
    if x1 < x2:
        x3 = x1 + l
        x4 = x1
        
        if y1 < y2:
            y3 = y1    
            y4 = y1 + l
        else:
            y3 = y1    
            y4 = y1 - l

    else:
        x3 = x1 - l
        x4 = x1
        
        if y1 < y2:
            y3 = y1    
            y4 = y1 + l
        else:
            y3 = y1    
            y4 = y1 - l

if error:
    print(-1)
else:
    print(x3 - delta, y3 - delta, x4 - delta, y4- delta)

'''
0 0 2 0
0 2 2 2

0 1 2 3
0 3 2 1


-100 -100 99 100
-1

27 -74 27 74
175 -74 175 74

-100 100 100 -100
-100 -100 100 100


'''