import sys
num, want = map(int, sys.stdin.readline().rstrip().split(" "))
medal_list = []
want_nation = []
result = 1
for i in range(0,num):
    national_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if national_list[0] != want:
        medal_list.append(national_list)
    else:
        want_nation = national_list

for i in medal_list:
    if i[1] > want_nation[1]:
        result += 1
    elif i[1] == want_nation[1]:
        if i[2] > want_nation[2]:
            result += 1
        elif i[2] == want_nation[2]:
            if i[3] > want_nation[3]:
                result += 1
            else:
                continue
    else:
        continue

print(result)