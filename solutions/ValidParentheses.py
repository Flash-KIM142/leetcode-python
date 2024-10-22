class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        stk = []
        for c in chars:
            if stk:
                if stk[-1] == '(' and c == ')':
                    stk.pop()
                elif stk[-1] == '{' and c == '}':
                    stk.pop()
                elif stk[-1] == '[' and c == ']':
                    stk.pop()
                else:
                    stk.append(c)
            else:
                stk.append(c)

        if not stk:
            return True
        return False


solution = Solution()
print(solution.isValid("()"))
