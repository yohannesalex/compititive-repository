# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

import sys
from collections import defaultdict




t = int(input())
for i in range(t):
    n = int(input())
    LRU = input()
    mp = defaultdict(list)
    for i in range(1, n + 1):
        left, right = map(int, input().split())
        mp[i].extend((left, right))
    

    def dfs():
        ans = float('inf')
        stack = [(1, 0)]
        while stack:
            curr, cost = stack.pop()
            
            if curr == 0:
                continue
            
            left, right = mp[curr]
            if not left and not right:
                ans = min(ans, cost)
                continue
            if left:
                if LRU[curr - 1] != "L":
                    stack.append((left,cost+1))
                else:
                    stack.append((left,cost))
                
            if right:
                if LRU[curr - 1] != "R":
                    stack.append((right,cost+1))
                else:
                    stack.append((right,cost))
        return ans
    
    
    ans = dfs()
    print(ans)
