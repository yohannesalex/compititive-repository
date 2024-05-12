# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def find_numbers(m, s):
    if s == 0:
        if m == 1:
            return 0, 0
        else:
            return -1, -1
    if s > 9 * m:
        return -1, -1
    
    
    min_num = 1
    min_digits = [0] * m
    min_digits[0] = 1
    remaining_sum = s - 1
    i = m - 1
    while remaining_sum > 0:
        add = min(9, remaining_sum)
        min_digits[i] += add
        remaining_sum -= add
        i -= 1
    
   
    max_digits = [0] * m
    remaining_sum = s
    i = 0
    while remaining_sum > 0:
        add = min(9, remaining_sum)
        max_digits[i] += add
        remaining_sum -= add
        i += 1
    
    return int(''.join(map(str, min_digits))), int(''.join(map(str, max_digits)))


m, s = map(int, input().split())

min_num, max_num = find_numbers(m, s)
print(min_num, max_num)
