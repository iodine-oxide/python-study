pivo = [0,1]
a = int(input())
for i in range(1,a):
    current_number = pivo[i] + pivo[i-1]
    pivo.append(current_number)
print(pivo[a])