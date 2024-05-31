# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque


n = int(input())
names = []

for i in range(n):
    names.append(input())

indegree = defaultdict(int)
graph = defaultdict(list)

alpha = set()
flagg = False
for i in range(n-1):
    word1 = names[i]
    word2 = names[i+1]
    
    j = 0
    while j<len(word1) and j<len(word2):
        if word1[j]!=word2[j]: 
            if word2[j] not in graph[word1[j]]:
                graph[word1[j]].append(word2[j])
                alpha.add(word1[j])
                alpha.add(word2[j])
                indegree[word2[j]]+=1
            break
        else:
            if j + 1 >= len(word2) and j + 1 < len(word1):
                flagg = True
        j+=1


que = deque()

for char in alpha:
    if indegree[char] == 0:
        que.append(char)

res = []
while que:
    node = que.popleft()
    res.append(node)
    
    for neb in graph[node]:
        indegree[neb] -= 1
        if indegree[neb] == 0:
            que.append(neb)
m = len(graph)
# print(res)

ans = []

alphabet = 'abcdefghijklmnopqrstuvwxyz'
flag = True
for i in range(len(alphabet)):
    if flag and alphabet[i] in res:
        flag = False
        ans.extend(res)
    elif alphabet[i] not in res:
        ans.append(alphabet[i])





if len(ans) == len(alphabet) and len(res) == m and not flagg:
    print("".join(ans))
else:
    print("Impossible")