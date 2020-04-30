import sys
input = sys.stdin.readline

n = int(input())

def intl():
    return(list(map(int,input().split())))
nums = intl()

even = False
found = False

if nums[0] %2 == 0 and nums[1] %2 == 0:
    even = True
elif nums[1] %2 == 0 and nums[2] %2 == 0:
    even = True
elif nums[0] %2 == 0 and nums[2] %2 == 0:
    even = True


for i, num in enumerate(nums):
    this_even = num %2 == 0
    if even != this_even:
        print(i+1)
        found = True
        break
    # print('num = ', num)

if not found:
    print(1)

'''

o

8 6 7 8
o

9 4 6 8
e
e
'''