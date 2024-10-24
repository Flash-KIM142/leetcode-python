from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0
        gene_options = ['A', 'C', 'G', 'T']
        visited = set()
        bank = set(bank)
        q = deque()
        q.append(startGene)
        cnt = 0
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == endGene:
                    return cnt
                for j in range(8):
                    for g in gene_options:
                        newGene = cur[:j] + g + cur[j + 1:]
                        if newGene in bank and newGene not in visited:
                            q.append(newGene)
                            visited.add(newGene)
            cnt += 1
        return -1
