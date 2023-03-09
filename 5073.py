comp_list = []
while True:
    three = input()
    a, b, c = int(three.split(" ")[0]), int(three.split(" ")[1]), int(three.split(" ")[2])
    if a == 0 and b == 0 and c == 0:
        for i in comp_list:
            if max(i) < (sum(i) - max(i)):
                if len(set(i)) == 1:
                    print("Equilateral")
                elif len(set(i)) == 2:
                    print("Isosceles")
                else:
                    print("Scalene")
            else:
                print("Invalid")
        break
    var_list = [a, b, c]
    comp_list.append(var_list)