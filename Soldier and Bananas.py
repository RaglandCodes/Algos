'''
Codeforces  A. Soldier and Bananas
'''
ip = input().split()

k = int(ip[0])
n = int(ip[1])
w = int(ip[2])

price = 0

for i in range(1, w+1):
    price += (k*i)

if price>n:
    print(price - n)
else:
    print(0)
