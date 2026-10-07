class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1

                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}

        while queue:

            result = []

            # Check current level
            for string in queue:
                if isValid(string):
                    result.append(string)

            # First valid level = minimum removals
            if result:
                return result

            # Generate next level
            next_level = set()

            for string in queue:
                for i in range(len(string)):

                    # Remove only parentheses
                    if string[i] in "()":
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            queue = next_level

        return [""]