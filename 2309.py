list_of_dwarf = []
for i in range (0,9):
    heights = int(input())
    list_of_dwarf.append(heights)
list_of_dwarf.sort()
i = 0
j = -1
while True:
    if sum(list_of_dwarf)-100 > list_of_dwarf[i] + list_of_dwarf[j]:
        i+=1
    elif sum(list_of_dwarf)-100 < list_of_dwarf[i] + list_of_dwarf[j]:
        j-=1
    else:
        list_of_dwarf.pop(i)
        list_of_dwarf.pop(j)
        break
for k in list_of_dwarf:
    print(k)