jnum, bnum = input().split()
jnum = int(jnum)
bnum = int(bnum)
result = 0
j_list = [[0 for i in range(0, 2)]for j in range(0, jnum)]
b_list = [[0 for k in range(0, 3)]for l in range(0, bnum)]
for i in range (0,jnum):
    jweight, jvalue = input().split()
    j_list[i][0] = int(jweight)
    j_list[i][1] = int(jvalue)
for i in  range (0,bnum):
    b_list[i][0] = int(input())
j_list.sort(key = lambda x:x[1])
b_list.sort(key = lambda x:x[0])
j = 0
for i in range (0, jnum):
    if b_list[j][0] > j_list[i][0] and b_list[j][1] < j_list[i][1]:
        b_list[j][1] = j_list[i][1]
        b_list[j][2] = j_list[i][0]
        result += j_list[i][0]
        break
print(result)