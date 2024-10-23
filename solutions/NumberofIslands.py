from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for i in range(row)]
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        answer = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '0':
                    continue
                if visited[r][c]:
                    continue
                q.append([r, c])
                visited[r][c] = True
                answer += 1
                while q:
                    cur = q.popleft()
                    cur_r = cur[0]
                    cur_c = cur[1]
                    for d in range(4):
                        nxt_r = cur_r + dir[d][0]
                        nxt_c = cur_c + dir[d][1]
                        if nxt_r < 0 or nxt_r >= row or nxt_c < 0 or nxt_c >= col:
                            continue
                        if visited[nxt_r][nxt_c]:
                            continue
                        if grid[nxt_r][nxt_c] == '0':
                            continue
                        q.append([nxt_r, nxt_c])
                        visited[nxt_r][nxt_c] = True

        return answer
