# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict

n, edge = map(int, input().split())
graph = defaultdict(list)
List = set()

for _ in range(edge):
    n, m = map(int, input().split())
    List.add(n)
    List.add(m)
    graph[n].append(m)
    graph[m].append(n)
visited= set()

def dfs(node, parent):
   
    global visited
    stack=[]
    stack.append(node)
    visited.add(node)
    res = True
    while stack:
        node = stack.pop()
        if len(graph[node]) != 2:
            res = False
        for negn in graph[node]:
            if negn not in visited:
            
                stack.append(negn)
                visited.add(negn)
                
                
    return res

count = 0
for i in List:
    
    if i not in visited:
        if dfs(i, -1):  
            count += 1

print(count)
