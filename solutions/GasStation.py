from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total_gas = 0
        total_cost = 0
        cur_gas = 0
        start = 0

        for i in range(N):
            total_gas += gas[i]
            total_cost += cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas<0:
                start = i+1
                cur_gas=0

        if total_gas<total_cost:
            return -1
        return start