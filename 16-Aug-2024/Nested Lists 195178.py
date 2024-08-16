# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score,name])
    records.sort()
    lowest = records[1][0]
    for i in records:
        if i[0] == lowest:
            print(i[1])