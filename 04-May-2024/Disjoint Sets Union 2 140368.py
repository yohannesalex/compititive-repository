# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n , t = list(map(int,input().split()))
root= [i for i in range(n+1)]
size = [1]*(n+1)
mini = [i for i in range(n+1)]
maxi = [i for i in range(n+1)]
def find(x):
    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]
    return x

 
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX != rootY:
        
        root[rootX] = rootY
        mini[rootY] = min(mini[rootX], mini[rootY])
        maxi[rootY] = max(maxi[rootX], maxi[rootY])
        size[rootY] += size[rootX]

for i in range(t):
    query= list(input().split())
    if query[0] == "union":
        union(int(query[1]),int(query[2]))
    else:
        
        num = find(int(query[1]))
        
        
        print(mini[num],maxi[num],size[num]) 
        

