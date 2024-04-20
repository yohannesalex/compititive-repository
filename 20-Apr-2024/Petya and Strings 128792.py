# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A


st1 = input()
st2 = input()
flag = True
for i in range(len(st1)):
    if ord(st1[i].lower()) > ord(st2[i].lower()):
        print(1)
        flag= False
        break
    elif ord(st1[i].lower()) < ord(st2[i].lower()):
        print(-1)
        flag = False
        break
if flag:
    print(0)
