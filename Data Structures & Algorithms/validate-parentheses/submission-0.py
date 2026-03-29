class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapz = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapz.values():
                stack.append(char)
            elif char in mapz:
                if not stack or stack[-1] != mapz[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack 
        