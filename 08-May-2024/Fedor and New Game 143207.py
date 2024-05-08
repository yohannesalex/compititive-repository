# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n , m , k = list(map(int,input().split()))
nums = []
for i in range(m):
    nums.append(int(input()))
fedor =int(input())
check = [0]*m
for i in range(32):
    fed_bit = fedor & 1<<i
    for j  in range(len(nums)):
        if nums[j] & 1<<i != fed_bit:
            check[j]+=1
res=0
for i in range(m):
    if check[i] <= k:
        res+=1
print(res)




