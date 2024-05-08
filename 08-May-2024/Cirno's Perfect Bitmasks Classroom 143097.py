# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())

for i in range(t):
    s = ""
    num = int(input())
    count = 0
    for i in range(32):
        if num & 1<< i:
            count+=1
    

    for i in range(32):
        if num & 1<< i:
            s= "1"+ s
            break
        else:
            s = "0"+ s
    
    if count > 1:
        print(int(s,2))
    else:
        cur = int(s,2)
        for i in range(32):
            if not num & (1<<i):
                cur|=(1<<i)
                break
        print(int(cur))
