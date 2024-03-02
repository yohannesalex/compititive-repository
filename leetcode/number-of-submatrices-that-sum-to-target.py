class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0 
        sum_matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):
                top = sum_matrix[row - 1][col] if row > 0 else 0
                left = sum_matrix[row][col - 1] if col > 0 else 0
                top_left = sum_matrix[row - 1][col - 1] if min(row, col) > 0 else 0
                
                sum_matrix[row][col] += top + left - top_left
        
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                hash_sum = defaultdict(lambda : 0)
                hash_sum[0] += 1
                for c in range(COLS):
                    sums = sum_matrix[r2][c] - (sum_matrix[r1 - 1][c] if r1 > 0 else 0)
                    diff = sums - target
                    if diff in hash_sum:
                        result += hash_sum[diff]
                    hash_sum[sums] += 1
        
        return result
                
                
