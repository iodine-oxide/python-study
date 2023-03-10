dict = {}
word = input()
alphabet = list(word)
for i in alphabet:
    try: dict[i.upper()] += 1
    except: dict[i.upper()] = 1
value_list = list(dict.values())
key_list = list(dict.keys())
value_list1 = sorted(value_list, reverse=True)
if len(value_list1)>1 and value_list1[0] == value_list1[1]:
    print("?")
else:
    index = value_list.index(max(value_list))
    print(key_list[index])