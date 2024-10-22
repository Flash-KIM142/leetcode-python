from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, v in enumerate(nums):
            if nums[i] != val:
                nums[k] = v
                k += 1

        return k
