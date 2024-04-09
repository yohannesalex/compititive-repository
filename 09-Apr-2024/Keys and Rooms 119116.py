# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]
        que=deque()
        que.append(0)
        visited = set()
        while que:
            node = que.popleft()
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    que.append(neigh)

        if len(visited) == len(rooms):
            return True
        return False

            