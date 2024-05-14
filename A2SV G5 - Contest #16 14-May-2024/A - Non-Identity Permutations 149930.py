# Problem: A - Non-Identity Permutations - https://codeforces.com/gym/523525/problem/A


t = int(input())
for i in range(t):
    n = int(input())
    nums = []
    for i in range(1,n+1):
        nums.append(i)
    cur = nums.copy()
    cur.reverse()
    flag = True
    if len(nums)%2 == 0:
        print(*cur)
        flag = False
    else:
        if flag:    
            cur[len(nums)//2] , cur[len(nums)//2+1] = cur[len(nums)//2+1], cur[len(nums)//2]
            print(*cur)


  