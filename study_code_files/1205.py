import sys
Num, score, con = map(int, sys.stdin.readline().rstrip().split(" "))
ranking_list = list
if Num > 0:
    ranking_list = list(map(int, sys.stdin.readline().rstrip().split()))
    if score <= min(ranking_list) and len(ranking_list) <= con:
        print(-1)
    else:
        ranking_list.append(score)
        ranking_list.sort(reverse = True)
        rank = ranking_list.index(score) + 1
        print(rank)
else:
    if con>0:
        print(1)
    else:
        print(-1)