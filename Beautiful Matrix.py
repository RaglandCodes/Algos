'''

Codeforces A. Beautiful Matrix

'''

matrix = []
one_i = 0
one_j = 0

for i in range(0, 5):
    row = input().split()
    row = [int(i) for i in row]
    if 1 in row:
        one_i = i
        one_j = row.index(1)
    matrix.append(row)

print(abs(2 - one_i) + abs(2 - one_j))