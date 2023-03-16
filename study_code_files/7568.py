import sys
people_list = []
num = int(sys.stdin.readline().rstrip())

for i in range(0,num):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    people_list.append([a[0], a[1], 1])

for i in people_list:
    for j in people_list:
        if i[0] < j[0] and i[1] < j[1]:
            i[2] = i[2]+1
        else:
            continue

for i in people_list:
    print(i[2], end=" ")