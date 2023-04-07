import sys
mem, game = sys.stdin.readline().rstrip().split(" ")
play_list = set()
game_list = {"Y" : 2, "F" : 3, "O" : 4}
for i in range(int(mem)):
    name = sys.stdin.readline().rstrip()
    play_list.add(name)
print(len(play_list)//(game_list[game]-1))
