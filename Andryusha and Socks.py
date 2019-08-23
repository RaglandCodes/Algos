n = int(input())

table = []
max_table = 0
len_table = 0
ip = input().split()


for sock in ip:
    if sock in table:
        table.remove(sock)
        len_table -= 1
    else:
        table += [sock]
        len_table += 1
        max_table = max(len_table, max_table)
print(max_table)

