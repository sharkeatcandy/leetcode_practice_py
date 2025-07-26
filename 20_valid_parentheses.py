# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def check_parentheses(self, left_parentheses, right_parentheses):
        if left_parentheses == "(" and right_parentheses == ")":
            return True
        elif left_parentheses == "[" and right_parentheses == "]":
            return True
        elif left_parentheses == "{" and right_parentheses == "}":
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        i = 0
        end = len(s)
        if end % 2 != 0:
            return False
        while i + 1 < end:
            if self.check_parentheses(s[i], s[i + 1]):
                s = s[:i] + s[i + 2 :]
                end = len(s)
                if i > 1:
                    i -= 1
            else:
                i += 1

        i = 0
        end = len(s)
        while i < end:
            if self.check_parentheses(s[i], s[len(s) - i - 1]):
                end -= 1
                i += 1
                continue
            else:
                return False

        return True
