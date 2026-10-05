class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)

            else:
                curr = stack.pop()

                if s[i - 1] == '(':
                    curr = 1
                else:
                    curr = 2 * curr

                stack[-1] += curr

        return stack[0]