# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def fun():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        possible = True
        swaps = 0
        def mergeSort(left, right, arr):
            nonlocal possible 
            nonlocal swaps
            if left+1>=right: 
                return [arr[left]]
            mid = (right+left)//2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid, right, arr)

            if left_half[-1]<=right_half[0]:
                return left_half+right_half
            elif right_half[-1]<= left_half[0]:
                swaps+=1
                return right_half + left_half
            else:
                possible = False
                return left_half+right_half 
        
        mergeSort(0, n, arr)
        if possible:
            print(swaps)
        else:
            print(-1)
fun()