import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        self.make_a_combination(result, 0, 1, [], n, k)
        return result

    def make_a_combination(self, result: List[List[int]], cnt: int, idx: int, cur: List[int], n: int, k: int) -> None:
        if cnt == k:
            tmp = copy.deepcopy(cur)
            result.append(tmp)
            return

        for i in range(idx, n + 1):
            cur.append(i)
            self.make_a_combination(result, cnt + 1, i + 1, cur, n, k)
            cur.pop()
