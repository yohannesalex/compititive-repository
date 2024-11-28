# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from typing import List
from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Deque for 0-1 BFS
        deque_queue = deque([(0, 0, 0)])  # (row, col, obstacles_removed)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        while deque_queue:
            row, col, obstacles = deque_queue.popleft()
            
            # If we reach the bottom-right corner
            if row == m - 1 and col == n - 1:
                return obstacles
            
            # Explore all directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    if grid[new_row][new_col] == 0:
                        # Add to the front of the deque for zero-weight edges
                        deque_queue.appendleft((new_row, new_col, obstacles))
                    else:
                        # Add to the back of the deque for one-weight edges
                        deque_queue.append((new_row, new_col, obstacles + 1))
        
        return -1  # This case should never occur for a valid input
