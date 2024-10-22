class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = list(magazine)
        resources = dict()
        for c in magazine_chars:
            if not resources.get(c):
                resources[c] = 0
            resources[c] += 1

        ransomNote_chars = list(ransomNote)
        for c in ransomNote_chars:
            if resources.get(c, 0) > 0:
                resources[c] -= 1
            else:
                return False
        return True