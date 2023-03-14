import sys
rt_num = int(sys.stdin.readline().rstrip())
rt_dict = {}
fn_list = []
for i in range(0, rt_num):
    st_list = list(map(int, sys.stdin.readline().rstrip().split()))
    fn_list.append(st_list)

for j in fn_list:
    move = 0
    rt_key = j.pop(0)
    line = [j.pop(0)]
    for k in range(0,19):
        line.insert(0, j[k])
        loc = 0
        for l in range(1, len(line)):
            if line[l] < line[0]:
                continue
            else:
                loc = l
        line.insert(loc, line.pop(0))
        move += loc
    rt_dict[rt_key] = move

for i in rt_dict.items():
    print(*i)
