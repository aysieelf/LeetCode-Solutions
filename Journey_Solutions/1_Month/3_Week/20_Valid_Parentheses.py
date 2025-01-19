"""
Task:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
     determine if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

Examples:
    s = "()" => true
    s = "()[]{}" => true
    s = "([])" => true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}':'{'}
        stack = []
        for b in s:
            if stack and brackets.get(b) == stack[-1]:
                stack.pop()
            else:
                stack.append(b)

        return len(stack) == 0

sol = Solution()
s = "([])"
print(sol.isValid(s))
