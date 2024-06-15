# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from heapq import heapify, heappop, heappush
def answer():
    n = int(input())
    a = list(map(int, input().split()))
    heap = []
    for i in range(len(a)):
       if a[i] > 0:  heappush(heap, (-1*(a[i]), i+1))
    
    to_return = []
    while len(heap) >= 2:
        a, b = heappop(heap)
        c, d = heappop(heap)
        a *= -1
        c *= -1
        if a-1 > 0: heappush(heap, ((a-1)*-1, b))
        if c-1 > 0: heappush(heap, ((c-1)*-1, d))
        to_return.append([b, d])
    return to_return
    

m =int(input())
for _ in range(m):
    result = answer()
    print(len(result))
    for i in result: print(*i)