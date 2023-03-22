import sys
while True:
    right = 0
    word = sys.stdin.readline().rstrip()
    if word == "end":
        break
    vowel = ["a", "e", "i", "o", "u"]
    if len(word) == 1 and word in vowel:
        right = 0

    if len(word) == 2:
        if len(set(vowel).intersection(set(list(word)))) == 0:
                right += 1
    else:
        for i in range(0, len(word) - 2):
            if (word[i] == "e" and word[i + 1] == "e" and word[i+2] != "e") or (word[i] != "e" and word[i + 1] == "e" and word[i+2] == "e"):
                continue
            elif (word[i] == "o" and word[i + 1] == "o" and word[i+2]!="o") or (word[i] != "o" and word[i + 1] == "o" and word[i+2]=="o"):
                continue
            elif (word[i] == word[i+1]) or (word[i+1] == word[i+2]):
                right += 1
                break
            elif len(set(vowel).intersection(set(list(word)))) == 0:
                right += 1
                break
            elif ((word[i] in vowel) and (word[i+1] in vowel) and (word[i+2] in vowel)) or \
                    ((word[i] not in vowel) and (word[i+1] not in vowel) and (word[i+2] not in vowel)):
                right += 1
                break
            else:
                continue
    if right == 0:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
