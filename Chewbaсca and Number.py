'''

Codeforces 
A. Chewbaсca and Number
https://codeforces.com/problemset/problem/514/A

'''

num = list(input())
a = ""

for i, n in enumerate(num):
    # print("i = ", i)
    # print("n = ", n)
    # print("a = ", a)
    # print("------------------\n")
    if i == 0 and n == '9':
        a += '9'
        continue
    if n == '0' or n == '1' or n == '2' or n == '3' or n == '4':
        a += n
        continue

    if n == '5':
        a += '4'
    elif n == '6':
        a += '3'
    elif n == '7':
        a += '2'
    elif n == '8':
        a += '1'
    else:
         a += '0'
    
    
print(int(a))

