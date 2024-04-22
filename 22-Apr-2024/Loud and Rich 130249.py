# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
       
        n = len(quiet)
        out_d, least_q, answer, in_node = [0] * n, deepcopy(quiet), [i for i in range(n)], [[] for i in range(n)]
        q = deque()
        for a, b in richer:
            in_node[a].append(b)
            out_d[b] += 1
        for i in range(n):
            if out_d[i] == 0:
                q.append(i)
        while q:
            i = q.popleft()
            for nxt in in_node[i]:
                # print(i, nxt, quiet[i], least_q[nxt])
                out_d[nxt] -= 1
                if least_q[nxt] > least_q[i]:
                    least_q[nxt] = least_q[i]
                    answer[nxt] = answer[i]
                if out_d[nxt] == 0:
                    q.append(nxt)
        return answer
            



        