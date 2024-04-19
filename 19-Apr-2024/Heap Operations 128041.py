# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heappop, heappush

def process_operations(num_operations):
    heap = []
    correct_operations = []

    for _ in range(num_operations):
        operation_input = input().split()
        op = operation_input[0]

        if op == "insert":
            val = int(operation_input[1])
            heappush(heap, val)
            correct_operations.append(f"{op} {val}")
        elif op == "removeMin":
            if heap:
                heappop(heap)
            else:
                correct_operations.append("insert 0")
            correct_operations.append(op)
        else:
            val = int(operation_input[1])
            while heap and heap[0] < val:
                heappop(heap)
                correct_operations.append("removeMin")
            if not heap or heap[0] > val:
                heappush(heap, val)
                correct_operations.append(f"insert {val}")
            correct_operations.append(f"{op} {val}")

    return correct_operations

if __name__ == "__main__":
    num_operations = int(input())
    correct_operations = process_operations(num_operations)
    print(len(correct_operations))
    for op in correct_operations:
        print(op)
