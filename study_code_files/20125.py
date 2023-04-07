import sys
length = int(sys.stdin.readline().rstrip())
heart = []
size = []
head = 0
back = 0
lleg, rleg = 0, 0
rloc = 0
lloc = 0
for i in range(length):
    input_value = sys.stdin.readline().rstrip()
    if "_"*length == input_value:
        continue
    elif input_value.count("*")==1 and head == 0:
        head += 1
        heart.append(i+2)
        heart.append(input_value.find("*")+1)
    elif input_value.count("*")!=0 and head == 1:
        head+=1
        size.append(heart[1] - input_value.find("*")-1)
        size.append(input_value.count("*")-1-size[0])
    elif head == 2 and input_value.count("*") ==1:
        back+=1
        loc = input_value.find("*")
    elif head == 2 and input_value.count("*") ==2:
        head += 1
        lleg += 1
        rleg += 1
        lloc = input_value.find("*")
        rloc = lloc+2
        size.append(back)
    elif head == 3:
        loc = input_value.find("*")
        if input_value.count("*") == 2:
            lleg += 1
            rleg += 1
        elif input_value.count("*") == 1 and loc == lloc:
            lleg +=1
        else:
            rleg+=1

size.append(lleg)
size.append(rleg)

print(*heart)
print(*size)


