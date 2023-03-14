import sys

result_set = set()
list_number = ['1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
range_number = int(sys.stdin.readline().rstrip())
for i in range(0, range_number):
    order = sys.stdin.readline().rstrip()
    if order == "all":
        result_set.update(list_number)
    elif order == "empty":
        result_set.clear()
    else:
        real_order, num = order.split()
        if real_order == "remove":
            result_set.discard(num)
        elif real_order == "add":
            result_set.add(num)
        elif real_order == "check":
            if num in result_set:
                print(1)
            else:
                print(0)
        else:
            if num in result_set:
                result_set.remove(num)
            else:
                result_set.add(num)
