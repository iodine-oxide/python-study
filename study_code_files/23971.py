nums = input()
H, W, N, M = int(nums.split(" ")[0]), int(nums.split(" ")[1]), int(nums.split(" ")[2]), int(nums.split(" ")[3])
if ((W%(M+1)) != 0) & ((H%(N+1)) != 0):
    a = (W//(M+1))+1
    b = (H // (N + 1)) + 1
elif ((W%(M+1)) != 0) & ((H%(N+1)) == 0):
    a = (W // (M+1)) + 1
    b = (H // (N + 1))
elif ((W%(M+1)) == 0) & ((H%(N+1)) != 0):
    a = (W // (M+1))
    b = (H // (N + 1)) + 1
else:
    a = (W // (M + 1))
    b = (H // (N + 1))
print(int(a*b))