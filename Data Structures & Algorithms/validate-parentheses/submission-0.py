class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            elif ch in dic:
                if not stack or stack[-1] != dic[ch]:
                    return False   
                stack.pop()

        return not stack   # final answer (True/False)