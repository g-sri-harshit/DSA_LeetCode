class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Even the maximum possible opens became negative
            if high < 0:
                return False

            # Minimum cannot be negative
            low = max(low, 0)

        return low == 0