num = int(input())
a, i = 1, 1
count = 1
while a<num:
    a = a + 6*i
    i+=1
    count+=1
print(count)