stack = []
print_list = []
a = int(input())
i = 1
while i<=a:
    b = input().split()
    if b[0] == "push":
        stack.append(b[1])
    elif b[0] == "top":
        if len(stack) != 0:
            print_list.append(stack[-1])
        else:
            print_list.append(-1)
    elif b[0] == "pop":
        if len(stack) != 0:
            print_list.append(stack.pop(-1))
        else:
            print_list.append(-1)
    elif b[0] == "size":
        print_list.append(len(stack))
    else:
        if len(stack) != 0:
            print_list.append(0)
        else:
            print_list.append(1)
    i+=1
for j in print_list:
    print(j)