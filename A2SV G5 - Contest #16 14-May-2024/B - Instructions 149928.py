# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B


import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    
    def dp(i, n, memo):
        if i > n:
            return 0
        
        if i not in memo:
            memo[i] = nums[i-1] + dp(i + nums[i-1], n, memo)
            
        return memo[i]

    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        memo = {}
        max_score = 0
        for i in range(1, n+1):
            max_score = max(max_score, dp(i, n, memo))
        print(max_score)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
