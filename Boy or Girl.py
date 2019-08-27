'''

Codeforces A. Boy or Girl
https://codeforces.com/problemset/problem/236/A

'''

user_name_len = len(list(set(list(input()))))

if user_name_len%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")