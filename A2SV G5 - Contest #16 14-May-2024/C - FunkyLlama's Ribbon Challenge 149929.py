# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C


from os import name
import sys, threading


def main():
    def max_pieces(n, a, b, c, memo):
        if n == 0:
            return 0
        if n < 0:
            return float('-inf')
        if n in memo:
            return memo[n]
        
        
        pieces = 1 + max(max_pieces(n - a, a, b, c, memo),
                        max_pieces(n - b, a, b, c, memo),
                        max_pieces(n - c, a, b, c, memo))
        
        memo[n] = pieces
        return pieces
    n, a, b, c = map(int, input().split())
    memo = {}
    print(max_pieces(n, a, b, c, memo))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    